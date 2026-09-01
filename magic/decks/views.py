from django.shortcuts import render,redirect
from django.views.generic import View, DetailView, DeleteView
from .models import UserDeck,DeckCard   
from .forms import (DeckCreationForm)
from django.contrib.auth.mixins import LoginRequiredMixin
from card_search.models import Card
from django.http import JsonResponse
import json
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied

class DeckCreationView(LoginRequiredMixin,View):
    template_name = 'decks/deck_creation.html'
    login_url = 'login' 
    def get(self, request):
        form = DeckCreationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = DeckCreationForm(request.POST)
        if form.is_valid():
            deck = form.save(commit=False)  # D
            deck.user = request.user 
            deck.save()
            print(deck)
            print(deck.name)
            print(deck.format)
            print(deck.user)
            print(deck.id)
            return redirect('decks:deck_detail', pk=deck.id)
        return render(request, self.template_name, {'form': form})

class DeckDetailView(DetailView):
    model = UserDeck
    template_name = "decks/deck_detail.html"

class AddCardToDeckAPIView(LoginRequiredMixin, View):

    def post(self, request):
        try:
            data = json.loads(request.body)
            deck_id = data.get('deck_id')
            card_id = data.get('card_id')
            quantity = int(data.get('card_quantity', 1))
            
            if quantity < 1:
                return JsonResponse({'success': False, 'error': 'Quantity must be at least 1'}, status=400)
            
            deck = UserDeck.objects.get(pk=deck_id, user=request.user)
            card = Card.objects.get(pk=card_id)
            
            # Create or update DeckCard
            deckcard, created = DeckCard.objects.get_or_create(
                deck=deck, card=card,
                defaults={'quantity': quantity}
            )
            if not created:
                deckcard.quantity += quantity
                deckcard.save()
            
            return JsonResponse({'success': True, 'message': '✅ Added to deck'})
        
        except json.JSONDecodeError:
                return JsonResponse({'success': False, 'error': 'Invalid JSON'}, status=400)
        except (UserDeck.DoesNotExist, Card.DoesNotExist) as e:
            return JsonResponse({'success': False, 'error': f'{e.__class__.__name__}: not found'}, status=404)
        except ValueError as e:
            return JsonResponse({'success': False, 'error': f'Invalid input: {str(e)}'}, status=400)
        except Exception as e:
            return JsonResponse({'success': False, 'error': f'{e.__class__.__name__}: {str(e)}'}, status=400)
class AddCardToDeckView(LoginRequiredMixin, View):
    """
    Handles adding a card to a deck via AJAX/Fetch request
    URL: /decks/<int:pk>/add-card/
    Method: POST
    """
    
    def post(self, request, pk):
        try:
            # Get the deck (verify user owns it)
            deck = UserDeck.objects.get(pk=pk, user=request.user)
            
            # Parse JSON from request body
            data = json.loads(request.body)
            card_id = data.get('card_id')
            
            # Get the card
            card = Card.objects.get(id=card_id)
            
            # Add card to deck (ManyToMany)
            deck.card.add(card)
            
            # Return success response
            return JsonResponse({
                'success': True,
                'message': f'Added {card.name} to {deck.name}',
                'card': {
                    'id': card.id,
                    'name': card.name,
                    'type': card.type,
                    'image_uri': card.image_uri,
                    'rarity': card.rarity,
                    'set_name': card.set_name,
                }
            })
        
        except UserDeck.DoesNotExist:
            return JsonResponse(
                {'success': False, 'error': 'Deck not found'}, 
                status=404
            )
        except Card.DoesNotExist:
            return JsonResponse(
                {'success': False, 'error': 'Card not found'}, 
                status=404
            )
        except json.JSONDecodeError:
            return JsonResponse(
                {'success': False, 'error': 'Invalid JSON'}, 
                status=400
            )
        except Exception as e:
            return JsonResponse(
                {'success': False, 'error': str(e)}, 
                status=400
            )

class DeleteView(DeleteView):
    model = UserDeck
    success_url = reverse_lazy('dashboard')
    
    def get_object(self):
        obj = super().get_object()
        if obj.user != self.request.user:
            raise PermissionDenied()
        return obj