from django.shortcuts import render
from django.views.generic import ListView
from .models import Card
class Dashboard(ListView):
    model = Card
    template_name = 'blogapp/postlist.html'
    paginate_by = 5

    def get_queryset(self):
        return Card.objects.all()