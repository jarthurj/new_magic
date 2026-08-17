from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.views.generic import View
from .models import Card
from .forms import (DeckCreationForm)


class Search(View):
    template_name = 'decks/deck_creation.html'
    def get(self, request):
        form = DeckCreationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        return redirect('home')