from django import forms
from rest_framework.generics import get_object_or_404
from service_objects.services import ServiceWithResult

from models_app.models import Card


class CardRetrieveService(ServiceWithResult):
    pk = forms.IntegerField()

    def process(self):
        self.result = self._card
        return self

    @property
    def _card(self):
        card = get_object_or_404(Card, pk=self.cleaned_data['pk'])
        return card
