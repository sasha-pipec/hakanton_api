from rest_framework.response import Response
from rest_framework.views import APIView
from service_objects.services import ServiceOutcome

from api.serializers.card.serializers import CardSerializer
from api.services.card.list import CardListService


class CardListView(APIView):

    def get(self, request):
        outcome = ServiceOutcome(CardListService, request.data)
        return Response({
            'TOP': CardSerializer(outcome.result['TOP'], many=True).data,
            'BOTTOM': CardSerializer(outcome.result['BOTTOM'], many=True).data,
            'LEFT': CardSerializer(outcome.result['LEFT'], many=True).data,
            'RIGHT': CardSerializer(outcome.result['RIGHT'], many=True).data,
            'CORNER': CardSerializer(outcome.result['CORNER'], many=True).data,
        })
