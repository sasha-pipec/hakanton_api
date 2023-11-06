from django.urls import path

from api.views.cards import CardListView

urlpatterns = [
    path('cards/', CardListView.as_view())
]
