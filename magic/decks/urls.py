from django.urls import path
from django.contrib import admin
from .views import (DeckCreationView,DeckDetailView, 
                    AddCardToDeckView,AddCardToDeckAPIView,
                    DeleteView,DeckListView,DeckDetailViewPublic,
                    CopyDeckAPIView)

app_name = 'decks'

urlpatterns = [
    path("deck_creation/",DeckCreationView.as_view(),name="deck_creation"),
    path("<int:pk>/", DeckDetailView.as_view(), name="deck_detail"),
    path('<int:pk>/add-card/', AddCardToDeckView.as_view(), name='add_card'),
    path('<int:pk>/delete/',DeleteView.as_view(),name="delete"),
    path('api/add-card/', AddCardToDeckAPIView.as_view(), name='api_add_card'),
    path('api/copy-deck/', CopyDeckAPIView.as_view(), name='api_copy_deck'),
    path('decks_list/',DeckListView.as_view(), name='decks_list'),
    path('<int:pk>/detail_public/',DeckDetailViewPublic.as_view(), name="deck_detail_public")
]
