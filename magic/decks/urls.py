from django.urls import path
from django.contrib import admin
from .views import DeckCreationView,DeckDetailView

app_name = 'decks'

urlpatterns = [
    path("deck_creation/",DeckCreationView.as_view(),name="deck_creation"),
    path("<int:pk>/", DeckDetailView.as_view(), name="deck_detail"),
]
