from django import forms
from service_objects.fields import ModelField
from service_objects.services import ServiceWithResult

from models_app.models import User, Card


class UserStepService(ServiceWithResult):
    position = forms.IntegerField()
    user = ModelField(User)

    def process(self):
        self._position()
        self.result = {
            'user': self._user,
            "card_id": self._card_id
        }
        return self

    def _position(self):
        self._user.position += self.cleaned_data['position']
        if self._user.position > 40:
            self._user.position -= 40
        self._user.save()

    @property
    def _card_id(self):
        return Card.objects.get(index=self._user.position).id

    @property
    def _user(self):
        return self.cleaned_data['user']
