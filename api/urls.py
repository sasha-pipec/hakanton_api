from django.urls import path

from api.views.answer import AnswerCheckView
from api.views.cards import CardListCreateView, CardGetActionView
from api.views.user import UserRegisterView, UserLoginView, RoomUserListCreateView, UserShowView

urlpatterns = [
    path('users/register/', UserRegisterView.as_view()),
    path('users/login/', UserLoginView.as_view()),
    path('users/me/', UserShowView.as_view()),

    path('rooms/', CardListCreateView.as_view()),
    path('rooms/<int:id>/users/', RoomUserListCreateView.as_view()),
    path('rooms/<int:id>/cards/', CardListCreateView.as_view()),

    # path('rooms/<int:room_id>/cards/<int:id>/info/', CardInfoView.as_view()),
    path('cards/<int:pk>/action/', CardGetActionView.as_view()),

    path('rooms/<int:id>/answer/check/', AnswerCheckView.as_view()),
]
