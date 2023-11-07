from functools import lru_cache

from django import forms
from service_objects.services import ServiceWithResult, ServiceOutcome

from api.services.card.retrieve import CardRetrieveService
from models_app.models import Card, Question, Answer, Event


class CardActionService(ServiceWithResult):

    def process(self):
        self.result = self._action
        return self

    @property
    def _action(self):
        return Question.objects.all().order_by('?').first()
