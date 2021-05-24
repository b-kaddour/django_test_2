from django.db import models
from django.utils import timezone

# Create your models here.
class Ingredient(models.Model):
    nom = models.CharField(max_length=255)
    price = models.CharField(max_length=4)

    def __str__(self):
        return self.nom


class Recette(models.Model):
    titre = models.CharField(max_length=255)
    description = models.TextField()
    ingredient = models.TextField()
    ingredients = models.ManyToManyField(Ingredient)
    image_url = models.CharField(max_length=255)
    created_date = models.DateTimeField(default=timezone.now)
    # On précise que ce champs peut être null et vide
    published_date = models.DateTimeField(blank=True, null=True)

    # Permet d'intégrer la date de publication
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.titre


class Comment(models.Model):
    pseudo = models.CharField(max_length=255)
    comment = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
