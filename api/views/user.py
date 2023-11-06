from rest_framework.response import Response
from rest_framework.views import APIView
from service_objects.services import ServiceOutcome
from rest_framework.permissions import IsAuthenticated

from api.serializers.room.serializers import RoomSerializer
from api.services.room.add_user import RoomAddUserService
from api.serializers.user.serializers import UserSerializer
from api.services.user.create import UserRegisterService
from api.services.user.list_by_room import RoomUserListService
from api.services.user.login import UserLoginService


class UserRegisterView(APIView):

    def post(self, request, *args, **kwargs):
        outcome = ServiceOutcome(UserRegisterService, request.data)
        return Response({
            "key": outcome.result["key"],
            "user": UserSerializer(outcome.result["user"], many=False).data
        })


class UserLoginView(APIView):

    def post(self, request, *args, **kwargs):
        outcome = ServiceOutcome(UserLoginService, request.data)
        return Response({
            "key": outcome.result["key"],
            "user": UserSerializer(outcome.result["user"], many=False).data
        })


class UserShowView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        return Response(UserSerializer(request.user).data)


class RoomUserListCreateView(APIView):

    def get(self, request, *args, **kwargs):
        outcome = ServiceOutcome(RoomUserListService, kwargs)
        return Response(UserSerializer(outcome.result, many=True).data)

    def post(self, request, *args, **kwargs):
        outcome = ServiceOutcome(RoomAddUserService, kwargs | {'user': request.user})
        return Response(RoomSerializer(outcome.result, many=False).data)
