from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.views.generic import View, DetailView
from .models import UserDeck   
from .forms import (DeckCreationForm)
from django.contrib.auth.mixins import LoginRequiredMixin

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
            print(UserDeck.objects.get(id=11))
            return redirect('decks:deck_detail', pk=deck.id)
        return render(request, self.template_name, {'form': form})

class DeckDetailView(DetailView):
    model = UserDeck
    template_name = "decks/deck_detail.html"