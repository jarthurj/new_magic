from django.shortcuts import render
from django.views.generic import ListView,View,FormView
from .models import Card,SetCode
from .forms import (SetCodeForm)
class Home(ListView):
    model = Card
    template_name = 'card_search/home.html'
    paginate_by = 24

    def get_queryset(self):
        return Card.objects.all()


class Search(View):
    template_name = 'card_search/search.html'

    def get(self, request):
        form = SetCodeForm()
        return render(request, self.template_name, {'form': form, 'results': []})

    def post(self, request):
        form = SetCodeForm(request.POST)
        results = []

        if form.is_valid():
            # Get selected SetCode instance
            selected_set_code = form.cleaned_data['set_code']  # this is already a SetCode instance
            # Fetch all related Card objects
            results = selected_set_code.cards.all()

        return render(request, 'card_search/results.html', {'form': form, 'results': results})
    
