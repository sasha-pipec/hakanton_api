from rest_framework.response import Response
from rest_framework.views import APIView
from service_objects.services import ServiceOutcome

from api.serializers.card.serializers import CardSerializer
from api.serializers.event.serializers import EventSerializer
from api.serializers.question.serializers import QuestionSerializer
from api.services.card.action import CardActionService
from api.services.card.info import CardInfoService
from api.services.card.list import CardListService
from models_app.models import Event


class CardListView(APIView):

    def get(self, request):
        outcome = ServiceOutcome(CardListService, request.data)
        return Response({
            'TOP': CardSerializer(outcome.result.get('TOP', []), many=True).data,
            'BOTTOM': CardSerializer(outcome.result.get('BOTTOM', []), many=True).data,
            'LEFT': CardSerializer(outcome.result.get('LEFT', []), many=True).data,
            'RIGHT': CardSerializer(outcome.result.get('RIGHT', []), many=True).data,
            'CORNER': CardSerializer(outcome.result.get('CORNER', []), many=True).data,
        })


class CardGetActionView(APIView):

    def get(self, request, *args, **kwargs):
        outcome = ServiceOutcome(CardActionService, kwargs)
        if isinstance(outcome.result, Event):
            return Response(EventSerializer(outcome.result).data)
        else:
            return Response(QuestionSerializer(outcome.result).data)


class CardInfoView(APIView):

    def get(self, request, *args, **kwargs):
        outcome = ServiceOutcome(CardInfoService, request.data | kwargs)
        return Response()
