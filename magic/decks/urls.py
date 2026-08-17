from django.urls import path
from django.contrib import admin
from .views import DeckCreation

app_name = 'decks'

urlpatterns = [
    path("deck_creation/",DeckCreation.as_view(),name="deck_creation"),
]
