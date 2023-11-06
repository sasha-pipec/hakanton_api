from functools import lru_cache

from service_objects.fields import ModelField

from models_app.models import Card, User, UserCard, Room
from service_objects.services import ServiceWithResult
from django import forms
from rest_framework.exceptions import NotFound


class CardInfoService(ServiceWithResult):
    id = forms.IntegerField()
    room_id = forms.IntegerField()
    user = ModelField(User)

    custom_validations = ['card_presence', 'room_presence']

    def process(self):
        self.run_custom_validations()
        return self

    @property
    @lru_cache
    def _card(self):
        try:
            return Card.objects.get(id=self.cleaned_data['id'])
        except Card.DoesNotExist:
            return None

    @property
    @lru_cache
    def _room(self):
        try:
            return Room.objects.get(id=self.cleaned_data['room_id'])
        except Room.DoesNotExist:
            return None

    def _user_card(self):
        try:
            user_card = UserCard.objects.get(
                room=self._room,
                card=self._card,
                user=self.cleaned_data['user']
            )
            question = 1
        except UserCard.DoesNotExist:
            pass

    def card_presence(self):
        if not self._card:
            raise NotFound("Card with this id not found")

    def room_presence(self):
        if not self._room:
            raise NotFound("Room with this id not found")
