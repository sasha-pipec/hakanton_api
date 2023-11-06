from django.urls import path

from api.views.cards import CardListView, CardInfoView, CardGetActionView
from api.views.user import UserRegisterView, UserLoginView, RoomUserListView

urlpatterns = [
    path('users/register/', UserRegisterView.as_view()),
    path('users/login/', UserLoginView.as_view()),
    path('rooms/<int:id>/users/', RoomUserListView.as_view()),
    path('rooms/<int:id>/cards/', CardListView.as_view()),
    # path('rooms/<int:room_id>/cards/<int:id>/info/', CardInfoView.as_view()),
    path('cards/<int:pk>/action/', CardGetActionView.as_view()),
]
