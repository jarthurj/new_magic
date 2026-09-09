from django.db import models
from card_search.models import Card
from django.conf import settings
from django.db.models import Sum
import requests

class UserDeck(models.Model):
    FORMAT_CHOICES = [
            ('standard', 'Standard'),
            ('commander', 'Commander'),
        ]
    name = models.CharField(max_length=100)
    card = models.ManyToManyField(Card,related_name="cards", through="DeckCard",blank=True)
    private = models.BooleanField(default=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="decks",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    format = models.CharField(max_length=100,choices=FORMAT_CHOICES,null=True,blank=True)
    def make_public(self):
        pass
    def __str__(self):
        return self.name
    def total_cards(self):
        total = self.deckcards.aggregate(total=Sum('quantity'))['total']
        return total or 0

    def copy_deck(self,user):
        new_deck = UserDeck.objects.create(name = self.name,
                                           format = self.format,
                                           user = user)
        for c in self.deckcards.all():
            dc = DeckCard.objects.create(deck=new_deck,card=c.card,quantity=c.quantity)
            dc.save()
    def commander_compliant(self):
        legend = False
        for dc in self.deckcards.all():
            if not dc.card.commander_legal:
                return False
            if dc.quantity > 1:
                if "land" not in dc.card.type.type.lower():
                    return False
            if "legend" in dc.card.type.type.lower():
                legend = True
        if legend:
            return True
        return False

    def full_deck_price_estimate(self):
        total_price = 0
        for dc in self.deckcards.all():
            card_price = self.get_prices(dc.card.scryfall_id)['usd']
            if card_price:
                total_price += float(card_price)
        return total_price
    def get_prices(self,scryfall_id):
        
        headers = {
            'User-Agent': 'MagicDeckBuilder/1.0',
            'Accept': 'application/json'
        }
        response = requests.get(
            f'https://api.scryfall.com/cards/{scryfall_id}',
            headers=headers
        )
        data = response.json()
        prices = data['prices']
        return prices
class DeckCard(models.Model):
    deck = models.ForeignKey(UserDeck, on_delete=models.CASCADE,related_name="deckcards")
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        deck_name = self.deck.name
        card_name = self.card.name
        quantity = self.quantity
        stringer = f'Deck Name:{deck_name} Card Name:{card_name} quantity:{quantity}'
        return stringer