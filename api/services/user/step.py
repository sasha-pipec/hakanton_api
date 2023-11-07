from django import forms
from service_objects.fields import ModelField
from service_objects.services import ServiceWithResult

from models_app.models import User


class UserStepService(ServiceWithResult):
    position = forms.IntegerField()
    user = ModelField(User)

    def process(self):
        self._position()
        self.result = self._user
        return self

    def _position(self):
        if self.cleaned_data['position'] > 40:
            self._user.position = self.cleaned_data['position'] - 40
        else:
            self._user.position = self.cleaned_data['position']
        self._user.save()

    @property
    def _user(self):
        return self.cleaned_data['user']
