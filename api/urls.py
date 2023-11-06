from django.urls import path

from api.views.user import UserRegisterView, UserLoginView, RoomUserListView

urlpatterns = [
    path('users/register/', UserRegisterView.as_view()),
    path('users/login/', UserLoginView.as_view()),
    path('rooms/<int:id>/users/', RoomUserListView.as_view()),
]

