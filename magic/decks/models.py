from django.db import models
from card_search.models import Card
from django.conf import settings

# class Deck(models.Model):
#     name = models.CharField(max_length=100)
#     card = models.ManyToManyField(Card,related_name="cards",blank=True)
#     shared = models.BooleanField(default=False)
#     user = models.ManyToManyField(
#         settings.AUTH_USER_MODEL,
#         related_name="users",
#         blank=True,)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     source_deck = models.ForeignKey(
#         UserDeck,
#         on_delete=models.SET_NULL,
#         null=True,
#         blank=True,
#         related_name="copies",
#     )

#     def __str__(self):
#         return self.name

class UserDeck(models.Model):
    FORMAT_CHOICES = [
            ('standard', 'Standard'),
            ('commander', 'Commander'),
        ]
    name = models.CharField(max_length=100)
    card = models.ManyToManyField(Card,related_name="cards",blank=True)
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