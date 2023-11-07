from functools import lru_cache

from service_objects.fields import ModelField
from service_objects.services import ServiceWithResult
from rest_framework.exceptions import NotFound
from django import forms
from models_app.models import Room, Answer, User, Card, UserCard


class AnswerCheckService(ServiceWithResult):
    id = forms.IntegerField()
    answer_id = forms.IntegerField()
    card_id = forms.IntegerField()
    user = ModelField(User)

    custom_validations = ['room_presence', 'answer_presence', 'card_presence']

    def process(self):
        self.run_custom_validations()
        self.result = self._check()
        return self

    def _check(self):
        data = {
            'send': True,
            'card_color': None,
            'owner_balance': {
                'id': None,
                'balance': None
            },
            'current_balance': {
                'id': None,
                'balance': None
            },
            'new_user_step_id': None
        }
        users_in_room = self._room.users.all()
        for index, user in enumerate(users_in_room):
            if user == self._user and index != len(users_in_room) - 1:
                data['new_user_step_id'] = users_in_room[index + 1].id
            elif index == len(users_in_room) - 1:
                data['new_user_step_id'] = users_in_room[0].id

        if self._answer.is_correct:
            if self.user_card:
                data['send'] = False
            else:
                UserCard.objects.create(
                    room=self._room,
                    card=self._card,
                    user=self._user
                )
                data['card_color'] = self._user.color
        else:
            if self.user_card:
                self._user.balance -= self._card.cost
                self._user.save()
                self.user_card.user.balance += self._card.cost
                self.user_card.user.save()
                data['owner_balance']['id'] = self.user_card.user.id
                data['owner_balance']['balance'] = self.user_card.user.balance
            else:
                self._user.balance -= self._card.cost
                self._user.save()
            data['current_balance']['id'] = self._user.id
            data['current_balance']['balance'] = self._user.balance
        user_list = [user for user in users_in_room]
        walk_user_id = 0
        for index, user in enumerate(user_list):
            if user.is_walk:
                if index == len(user_list) - 1:
                    user_list[0].is_walk = True
                    user_list[0].save()
                    walk_user_id = user_list[0].id
                else:
                    user.is_walk = False
                    user.save()
                    user_list[index + 1].is_walk = True
                    user_list[index + 1].save()
                    walk_user_id = user_list[index + 1].id
                break
        data['walk_user_id'] = walk_user_id
        return data

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
    def _user(self):
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
            return Answer.objects.get(id=self.cleaned_data['answer_id'])
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
