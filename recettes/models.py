from django.db import models
from django.utils import timezone

# Create your models here.

PLATS = {
    'lasagnes':{'name':'Lasagnes'},
    'quiche':{'name':'Quiche Lorraine'},
    'pizza':{'name':'Pizza'},
}
RECETTE = [
    {'name': [PLATS['lasagnes']], 'price':'7,00','ingredients':'poivre,sel,parmesan,muscade râpée,basilic,thym,vin rouge,eau,purée de tomate,carotte,branche,céleri,gousses,ail'},
    {'name': [PLATS['quiche']], 'price':'8,25','ingredients':' poivre,sel,muscade,lait,lardons,pâte brisée,beurre,oeufs,crème fraîche'},
    {'name': [PLATS['pizza']], 'price':'9,50','ingredients':'citron,huile d\'olive,origan,pâte à pizza,tranches fines,saumon,crème fraîche épaisse,boules'},
]

# SQL

class Ingredient(models.Model):
    nom=models.CharField(max_length=255)
    price=models.CharField(max_length=4)

    def __str__(self):
        return self.nom

class Recette(models.Model):
    titre=models.CharField(max_length=255)
    description=models.TextField()
    ingredient=models.TextField()
    ingredients=models.ManyToManyField(Ingredient)
    image_url=models.CharField(max_length=255)
    created_date = models.DateTimeField(default=timezone.now)
    # On précise que ce champs peut être null et vide
    published_date = models.DateTimeField(blank=True, null=True)

    # Permet d'intégrer la date de publication
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.titre


