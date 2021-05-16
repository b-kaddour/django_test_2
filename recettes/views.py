from django.shortcuts import render
from django.http import HttpResponse
from .models import Recette
from .models import RECETTE


# Create your views here.
def index(request):
    recette = Recette.objects.all
    return render(request, 'recettes/index.html', {'recette': recette})
