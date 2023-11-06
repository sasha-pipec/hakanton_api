from rest_framework.response import Response
from rest_framework.views import APIView
from service_objects.services import ServiceOutcome

from api.serializers.user.serializers import UserListSerializer
from api.services.user.create import UserRegisterService
from api.services.user.list_by_room import RoomUserListService
from api.services.user.login import UserLoginService


class UserRegisterView(APIView):

    def post(self, request, *args, **kwargs):
        outcome = ServiceOutcome(UserRegisterService, request.POST)
        return Response({"key": outcome.result})


class UserLoginView(APIView):

    def post(self, request, *args, **kwargs):
        outcome = ServiceOutcome(UserLoginService, request.POST)
        return Response({"key": outcome.result})


class RoomUserListView(APIView):

    def get(self, request, *args, **kwargs):
        outcome = ServiceOutcome(RoomUserListService, kwargs)
        return Response(UserListSerializer(outcome.result, many=True).data)
