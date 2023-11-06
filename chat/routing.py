from django.urls import path

from .consumers import *

ws_urlpatterns = [
    path('ws/room/<int:id>/', WSChatRoomView.as_asgi())
]
