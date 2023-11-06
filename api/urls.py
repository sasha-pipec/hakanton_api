from django.urls import path

from api.views.cards import CardListView, CardGetActionView
from api.views.rooms import RoomCreateView
from api.views.user import UserRegisterView, UserLoginView, RoomUserListCreateView

urlpatterns = [
    path('users/register/', UserRegisterView.as_view()),
    path('users/login/', UserLoginView.as_view()),

    path('rooms/', RoomCreateView.as_view()),
    path('rooms/<int:id>/users/', RoomUserListCreateView.as_view()),
    path('rooms/<int:id>/cards/', CardListView.as_view()),

    # path('rooms/<int:room_id>/cards/<int:id>/info/', CardInfoView.as_view()),
    path('cards/<int:pk>/action/', CardGetActionView.as_view()),
]
