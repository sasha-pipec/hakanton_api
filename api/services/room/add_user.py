from functools import lru_cache

from django import forms
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from service_objects.fields import ModelField
from service_objects.services import ServiceWithResult

from models_app.models import User, Room

COLOR_LIST = ['#FFFA79', '#8AFF96', '#7DD0FF', '#F19DFF', '#FF6262']


class RoomAddUserService(ServiceWithResult):
    user = ModelField(User)
    id = forms.IntegerField()

    custom_validations = ['check_count_players', 'room_user_presence']

    def process(self):
        self.run_custom_validations()
        self.result = self._add_user
        return self

    @property
    def _add_user(self):
        room = self._room
        room.users.add(self.cleaned_data['user'])
        users = room.users.all()
        if users.count() == room.count_players:
            for user in users:
                user.color = COLOR_LIST.pop(-1)
                user.save()
            room.status = Room.STARTED
        room.save()
        return room

    @property
    @lru_cache()
    def _room(self):
        room = get_object_or_404(Room, pk=self.cleaned_data['id'])
        return room

    @property
    @lru_cache()
    def _room_users(self):
        users = self._room.users.all()
        return users

    def check_count_players(self):
        if self._room.count_players == self._room_users.count():
            raise ValidationError('Игроки уже набраны')

    def room_user_presence(self):
        if self._room_users.filter(id=self.cleaned_data['user'].id).exists():
            raise ValidationError('Игрок уже в комнате')
