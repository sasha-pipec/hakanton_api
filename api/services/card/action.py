from functools import lru_cache

from django import forms
from service_objects.services import ServiceWithResult, ServiceOutcome

from api.services.card.retrieve import CardRetrieveService
from models_app.models import Card, Question, Answer, Event


class CardActionService(ServiceWithResult):
    pk = forms.IntegerField()

    def process(self):
        self.result = self._action
        return self

    @property
    def _action(self):
        card = self._card
        if card.type == Card.DEFAULT:
            question = Question.objects.all().order_by('?').first()
            return question
        return Event.objects.all().order_by('?').first()

    @property
    def _card(self):
        return ServiceOutcome(CardRetrieveService, {'pk': self.cleaned_data['pk']}).result
