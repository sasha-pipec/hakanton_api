from functools import lru_cache

from service_objects.services import ServiceWithResult
from django import forms
from rest_framework.exceptions import NotFound
from models_app.models import Room


class RoomUserListService(ServiceWithResult):
    id = forms.IntegerField()

    custom_validations = ['room_presence', ]

    def process(self):
        self.run_custom_validations()
        self.result = self._room.users.all()
        return self

    @property
    @lru_cache
    def _room(self):
        try:
            return Room.objects.get(id=self.cleaned_data['id'])
        except Room.DoesNotExist:
            return None

    def room_presence(self):
        if not self._room:
            raise NotFound("Room with this id not found")
