from django.db import models
from card_search.models import Card
class Deck(models.Model):
    card = models.ManyToManyField(Card,related_name="cards",blank=True)