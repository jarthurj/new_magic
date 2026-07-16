from django.shortcuts import render
from django.views.generic import ListView,View,FormView
from .models import Card
from .forms import (CardSearchForm)

class Home(ListView):
    model = Card
    template_name = 'card_search/home.html'
    paginate_by = 24

    def get_queryset(self):
        return Card.objects.all()


class Search(View):
    template_name = 'card_search/search.html'

    def get(self, request):
        form = CardSearchForm()
        return render(request, self.template_name, {'form': form, 'results': []})

    def post(self, request):
        form = CardSearchForm(request.POST)
        results = []

        if form.is_valid():
            # Get selected SetCode instance
            set_name_selected_cards = form.cleaned_data['set_name']  # this is already a SetCode instance
            rarity_selected_cards = form.cleaned_data['rarity']
            cards = Card.objects.all()
            if set_name_selected_cards:
                cards = cards.filter(set_name=set_name_selected_cards)
            if rarity_selected_cards:
                cards = cards.filter(rarity=rarity_selected_cards)
            # Fetch all related Card objects


        return render(request, 'card_search/results.html', {'form': form, 'results': cards})
    
