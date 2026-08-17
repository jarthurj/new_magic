from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.views.generic import View
from .models import UserDeck   
from .forms import (DeckCreationForm)
from django.contrib.auth.mixins import LoginRequiredMixin

class DeckCreation(LoginRequiredMixin,View):
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
            return redirect('deck_detail', pk=deck.pk)
        return render(request, self.template_name, {'form': form})