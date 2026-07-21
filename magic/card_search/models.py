from django.db import models

url_base = "https://cards.scryfall.io/normal/"

class SetId(models.Model):
    set_id = models.CharField(max_length=50)

    def __str__(self):
        return self.set_id 
class SetCode(models.Model):
    set_code = models.CharField(max_length=50)

    def __str__(self):
        return self.set_code 
    
class SetName(models.Model):
    set_name = models.CharField(max_length=50)

    def __str__(self):
        return self.set_name

class Rarity(models.Model):
    rarity = models.CharField(max_length=50)

    def __str__(self):
        return self.rarity
class Color(models.Model):
    symbol = models.CharField(max_length=1)
    def __str__(self):
        return self.symbol
class ColorIdentity(models.Model):
    symbol = models.CharField(max_length=1)
    def __str__(self):
        return self.symbol
class Keywords(models.Model):
    keyword = models.CharField(max_length=50)
    def __str__(self):
        return self.keyword
class ManaCostColor(models.Model):
    symbol = models.CharField(max_length=1)
    quantity = models.IntegerField(null=True)
    def __str__(self):
        return self.symbol+self.quantity
    
class Type(models.Model):
    type =  models.CharField(max_length =100)
    def __str__(self):
        return self.type

class ReleasedAt(models.Model):
    release_date = models.DateTimeField(null=True)
    def __str__(self):
        return self.release_date
class Name(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    #query optimization
#probably remove blanks
class Card(models.Model):
    scryfall_id = models.CharField(max_length=100,null=True,blank=True)
    oracle_id = models.CharField(max_length=100,null=True,blank=True)
    image_uri = models.URLField(null=True,blank=True)#take out https://
    mana_cost_numeric = models.PositiveIntegerField(null=True,blank=True)
    cmc = models.DecimalField(null=True,blank=True,decimal_places=1,max_digits=10)#change to decimal field
    oracle_text = models.CharField(max_length=1000,null=True,blank=True)
    standard_legal = models.BooleanField(blank=True,null=True)
    commander_legal = models.BooleanField(blank=True,null=True)
    set_id = models.ForeignKey(SetId,on_delete=models.CASCADE,related_name="cards",blank=True,null=True)
    set_code = models.ForeignKey(SetCode,on_delete=models.CASCADE,related_name="cards",blank=True,null=True)
    set_name = models.ForeignKey(SetName,on_delete=models.CASCADE,related_name="cards",blank=True,null=True)#search field
    rarity = models.ForeignKey(Rarity,on_delete=models.CASCADE,related_name="cards",blank=True,null=True)#search field
    name = models.ForeignKey(Name,on_delete=models.CASCADE,related_name="cards",null=True)#search field
    released_at = models.ForeignKey(ReleasedAt,on_delete=models.CASCADE,related_name="cards",null=True,blank=True)
    colors = models.ManyToManyField(Color,related_name="cards",blank=True)#search field
    color_identity = models.ManyToManyField(ColorIdentity,related_name="cards",blank=True)
    keywords = models.ManyToManyField(Keywords,related_name="cards",blank=True)#search field
    mana_cost_color = models.ManyToManyField(ManaCostColor,related_name="cards",null=True,blank=True)
    type = models.ForeignKey(Type,on_delete=models.CASCADE,null=True,blank=True)#search field