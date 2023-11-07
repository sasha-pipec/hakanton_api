from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ValidationError
from service_objects.services import ServiceWithResult
from django import forms

from models_app.models import User


class UserRegisterService(ServiceWithResult):
    login = forms.CharField(min_length=4)
    password = forms.CharField(min_length=4)

    custom_validations = ["user_presence", ]

    def process(self):
        self.run_custom_validations()
        self.result = self._token(self._register)
        return self

    @property
    def _register(self):
        return User.objects.create_user(
            username=self.cleaned_data['login'],
            password=self.cleaned_data['password'],
        )

    @staticmethod
    def _token(user):
        return {
            'user': user,
            'key': Token.objects.create(user=user).key
        }

    def user_presence(self):
        if User.objects.filter(username=self.cleaned_data['login']):
            raise ValidationError("User with this username already exists")
