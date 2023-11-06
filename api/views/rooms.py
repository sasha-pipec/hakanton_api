from rest_framework.response import Response
from rest_framework.views import APIView
from service_objects.services import ServiceOutcome

from api.serializers.room.serializers import RoomSerializer
from api.services.room.create import RoomCreateService
from api.services.room.list import RoomListService


class RoomListCreateView(APIView):

    def get(self, request, *args, **kwargs):
        outcome = ServiceOutcome(RoomListService, {})
        return Response(RoomSerializer(outcome.result, many=True).data)

    def post(self, request, *args, **kwargs):
        outcome = ServiceOutcome(RoomCreateService, request.data | {'user': request.user})
        return Response(RoomSerializer(outcome.result, many=False).data)
