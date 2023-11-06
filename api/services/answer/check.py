from functools import lru_cache

from service_objects.fields import ModelField
from service_objects.services import ServiceWithResult
from rest_framework.exceptions import NotFound
from django import forms
from models_app.models import Room, Answer, User, Card, UserCard


class AnswerCheckService(ServiceWithResult):
    id = forms.IntegerField()
    answer_id = forms.CharField()
    card_id = forms.CharField()
    user = ModelField(User)

    custom_validations = ['room_presence', 'answer_presence', 'card_presence']

    def process(self):
        self.run_custom_validations()
        self._check()
        return self

    def _check(self):
        if self._answer.is_correct:
            if self.user_card:
                pass
            else:
                UserCard.objects.create(
                    room=self._room,
                    card=self._card,
                    user=self.user
                )
        else:
            self.user.balance = self.user.balance - 1000
            self.user.save()

    @property
    @lru_cache
    def user_card(self):
        try:
            return UserCard.objects.get(
                room=self._room,
                card=self._card
            )
        except UserCard.DoesNotExist:
            return None

    @property
    def user(self):
        return self.cleaned_data['user']

    @property
    @lru_cache
    def _room(self):
        try:
            return Room.objects.get(id=self.cleaned_data['id'])
        except Room.DoesNotExist:
            return None

    @property
    @lru_cache
    def _card(self):
        try:
            return Card.objects.get(id=self.cleaned_data['card_id'])
        except Card.DoesNotExist:
            return None

    @property
    @lru_cache
    def _answer(self):
        try:
            return Answer.objects.get(id=self.cleaned_data['id'])
        except Answer.DoesNotExist:
            return None

    def room_presence(self):
        if not self._room:
            raise NotFound('Room with this id not found')

    def answer_presence(self):
        if not self._answer:
            raise NotFound('Answer with this id not found')

    def card_presence(self):
        if not self._card:
            raise NotFound('Card with this id not found')
