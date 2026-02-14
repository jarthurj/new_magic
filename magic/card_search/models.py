from django.db import models

url_base = "https://cards.scryfall.io/normal/"

class SetId(models.Model):
    set_id = models.CharField(max_length=50)

class SetCode(models.Model):
    set_code = models.CharField(max_length=50)

class SetName(models.Model):
    set_name = models.CharField(max_length=50)

class Rarity(models.Model):
    rarity = models.CharField(max_length=50)

class Color(models.Model):
    color = models.CharField(max_length=50)
    symbol = models.CharField(max_length=1)

class ColorIdentity(models.Model):
    color = models.CharField(max_length=50)
    symbol = models.CharField(max_length=1)

class Keywords(models.Model):
    keyword = models.CharField(max_length=50)

class ManaCostColor(models.Model):
    color = models.CharField(max_length=50)
    symbol = models.CharField(max_length=1)

class Type(models.Model):
    type =  models.CharField(max_length =100)

class ReleasedAt(models.Model):
    release_date = models.DateTimeField(null=True)

class Name(models.Model):
    name = models.CharField(max_length=100)
#query optimization
class Card(models.Model):
    scryfall_id = models.CharField(max_length=100,null=True)
    oracle_id = models.CharField(max_length=100,null=True)
    tcgplayer_id = models.PositiveIntegerField(null=True)
    cardmarket_id = models.PositiveIntegerField(null=True)
    image_uri = models.URLField(null=True)#take out https://
    mana_cost_numeric = models.PositiveIntegerField(null=True)
    cmc = models.FloatField(null=True)
    oracle_text = models.CharField(max_length=1000,null=True)
    standard_legal = models.BooleanField(blank=True,null=True)
    commander_legal = models.BooleanField(blank=True,null=True)
    colors = models.ManyToManyField(Color,related_name="cards",blank=True)
    color_identity = models.ManyToManyField(ColorIdentity,related_name="cards",blank=True)
    keywords = models.ManyToManyField(Keywords,related_name="cards",blank=True)
    set_id = models.ForeignKey(SetId,on_delete=models.CASCADE,related_name="cards",blank=True,null=True)
    set_code = models.ForeignKey(SetCode,on_delete=models.CASCADE,related_name="cards",blank=True,null=True)
    set_name = models.ForeignKey(SetName,on_delete=models.CASCADE,related_name="cards",blank=True,null=True)
    rarity = models.ForeignKey(Rarity,on_delete=models.CASCADE,related_name="cards",blank=True,null=True)
    mana_cost_color = models.ManyToManyField(ManaCostColor,related_name="cards",null=True)
    name = models.ForeignKey(Name,on_delete=models.CASCADE,related_name="cards",null=True)
    released_at = models.ForeignKey(ReleasedAt,on_delete=models.CASCADE,related_name="cards",null=True)
