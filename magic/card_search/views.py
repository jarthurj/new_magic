from django.shortcuts import render,redirect
from django.views.generic import ListView,View,FormView,DetailView
from .models import Card
from .forms import (CardSearchForm)
from django.core.paginator import Paginator
from urllib.parse import urlencode

class Home(ListView):
    model = Card
    template_name = 'card_search/home.html'
    paginate_by = 24

    def get_queryset(self):
        return Card.objects.all()


class Results(View):
    paginate_by = 24
    def get(self, request):
        form = CardSearchForm(request.GET)
        cards = Card.objects.all()

        if form.is_valid():

            set_name_selected_cards = form.cleaned_data['set_name']
            rarity_selected_cards = form.cleaned_data['rarity']
            name_selected_cards = form.cleaned_data['name']
            type_selected_cards = form.cleaned_data['type']
            cmc_selected_cards = form.cleaned_data['cmc']
            keywords_selected_cards = form.cleaned_data['keywords']
            color_selected_cards = form.cleaned_data['color']
            if set_name_selected_cards:
                cards = cards.filter(set_name=set_name_selected_cards)

            if rarity_selected_cards:
                cards = cards.filter(rarity=rarity_selected_cards)

            if name_selected_cards:
                cards = cards.filter(name__name__icontains=name_selected_cards)

            if type_selected_cards:
                cards = cards.filter(type=type_selected_cards)

            if cmc_selected_cards:
                cards = cards.filter(cmc=cmc_selected_cards)

            if keywords_selected_cards :
                cards = cards.filter(keywords=keywords_selected_cards)

            if color_selected_cards:
                cards = cards.filter(colors=color_selected_cards)

        paginator = Paginator(cards, self.paginate_by)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        query = request.GET.copy()

        query.pop("page", None)

        return render(request, 'card_search/results.html', {
            'form': form,
            'page_obj': page_obj,
            'query': query.urlencode()
        })

class Search(View):
    template_name = 'card_search/search.html'
    def get(self, request):
        form = CardSearchForm()
        return render(request, self.template_name, {'form': form})

class CardDetailView(DetailView):
    model = Card
    template_name = "card_search/card.html"