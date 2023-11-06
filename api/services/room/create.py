from django import forms
from service_objects.fields import ModelField
from service_objects.services import ServiceWithResult

from models_app.models import User, Room


class RoomCreateService(ServiceWithResult):
    user = ModelField(User)
    count_players = forms.IntegerField()
    title = forms.CharField()

    def process(self):
        self.result = self._create_room
        return self

    @property
    def _create_room(self):
        room = Room.objects.create(
            count_players=self.cleaned_data['count_players'],
            title=self.cleaned_data['title']
        )
        room.users.add(self.cleaned_data['user'])
        return room
