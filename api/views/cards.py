from rest_framework.response import Response
from rest_framework.views import APIView
from service_objects.services import ServiceOutcome

from api.serializers.card.serializers import CardSerializer
from api.serializers.event.serializers import EventSerializer
from api.serializers.question.serializers import QuestionSerializer
from api.serializers.room.serializers import RoomSerializer
from api.services.card.action import CardActionService
from api.services.card.info import CardInfoService
from api.services.card.list import CardListService
from api.services.room.create import RoomCreateService
from models_app.models import Event


class CardListCreateView(APIView):

    def get(self, request, *args, **kwargs):
        outcome = ServiceOutcome(CardListService, request.data)
        context = {
            "user": request.user,
            "room_id": kwargs['id'],
        }
        return Response({
            'TOP': CardSerializer(outcome.result.get('TOP', []), many=True, context=context).data,
            'BOTTOM': CardSerializer(outcome.result.get('BOTTOM', []), many=True, context=context).data,
            'LEFT': CardSerializer(outcome.result.get('LEFT', []), many=True, context=context).data,
            'RIGHT': CardSerializer(outcome.result.get('RIGHT', []), many=True, context=context).data,
            'CORNER': CardSerializer(outcome.result.get('CORNER', []), many=True, context=context).data,
        })

    def post(self, request, *args, **kwargs):
        outcome = ServiceOutcome(RoomCreateService, request.data | {'user': request.user})
        return Response(RoomSerializer(outcome.result, many=False).data)


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
