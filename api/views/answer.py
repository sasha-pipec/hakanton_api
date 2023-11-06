from rest_framework.response import Response
from rest_framework.views import APIView
from service_objects.services import ServiceOutcome

from api.services.answer.check import AnswerCheckService


class AnswerCheckView(APIView):

    def post(self, request, *args, **kwargs):
        outcome = ServiceOutcome(AnswerCheckService, request.data | kwargs)
        return Response()
