from rest_framework.response import Response
from rest_framework.views import APIView
from service_objects.services import ServiceOutcome

from api.serializers.room.serializers import RoomSerializer
from api.services.room.create import RoomCreateService
from api.services.room.list import RoomListService
from models_app.models import Room


class RoomListCreateView(APIView):

    def get(self, request, *args, **kwargs):
        outcome = ServiceOutcome(RoomListService, {})
        room = request.user.room_set.filter(status=Room.STARTED)
        return Response({
            'rooms': RoomSerializer(outcome.result, many=True, context={'user': request.user}).data,
            'room_id_to_current_user': room.first().id if room.exists() else None
        })

    def post(self, request, *args, **kwargs):
        outcome = ServiceOutcome(RoomCreateService, request.data | {'user': request.user})
        return Response(RoomSerializer(outcome.result, many=False, context={'user': request.user}).data)
