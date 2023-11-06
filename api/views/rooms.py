from rest_framework.response import Response
from rest_framework.views import APIView
from service_objects.services import ServiceOutcome

from api.serializers.room.serializers import RoomSerializer
from api.services.room.create import RoomCreateService


class RoomCreateView(APIView):

    def post(self, request, *args, **kwargs):
        outcome = ServiceOutcome(RoomCreateService, request.data | {'user': request.user})
        return Response(RoomSerializer(outcome.result, many=False).data)
