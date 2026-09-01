from django.urls import path
from django.contrib import admin
from .views import (DeckCreationView,DeckDetailView, 
                    AddCardToDeckView,AddCardToDeckAPIView,
                    DeleteView,DeckListView)

app_name = 'decks'

urlpatterns = [
    path("deck_creation/",DeckCreationView.as_view(),name="deck_creation"),
    path("<int:pk>/", DeckDetailView.as_view(), name="deck_detail"),
    path('<int:pk>/add-card/', AddCardToDeckView.as_view(), name='add_card'),
    path('<int:pk>/delete/',DeleteView.as_view(),name="delete"),
    path('api/add-card/', AddCardToDeckAPIView.as_view(), name='api_add_card'),
    path('decks_list/',DeckListView.as_view(), name='decks_list')
]
