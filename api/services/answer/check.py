from service_objects.services import ServiceWithResult
from django import forms

class AnswerCheckService(ServiceWithResult):
    id = forms.IntegerField()

    def process(self):

        return self
