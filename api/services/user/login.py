from functools import lru_cache

from django import forms
from rest_framework.authtoken.models import Token
from service_objects.services import ServiceWithResult
from rest_framework.exceptions import NotFound, AuthenticationFailed

from models_app.models import User


class UserLoginService(ServiceWithResult):
    login = forms.CharField(min_length=4)
    password = forms.CharField(min_length=4)

    custom_validations = ['user_presence', 'check_password']

    def process(self):
        self.run_custom_validations()
        self.result = self._token
        return self

    @property
    def _token(self):
        return Token.objects.get(user=self._user).key

    @property
    @lru_cache
    def _user(self) -> [User, None]:
        try:
            User.objects.get(username=self.cleaned_data['username'])
        except User.DoesNotExist:
            return None

    def user_presence(self):
        if not self._user:
            raise NotFound("User with this username does not exist")

    def check_password(self):
        if self._user.check_password(self.cleaned_data['password']):
            raise AuthenticationFailed("The password is not correct")
