from django.shortcuts import render
from django.views.generic import ListView
from .models import Card

class Home(ListView):
    model = Card
    template_name = 'card_search/home.html'
    paginate_by = 24

    def get_queryset(self):
        return Card.objects.all()