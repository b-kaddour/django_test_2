from django.shortcuts import render
from django.http import HttpResponse, Http404

from .models import Recette
from .models import Comment


# Create your views here.
def index(request):
    recette = Recette.objects.all
    return render(request, 'recettes/index.html', {'recette': recette})


# Création de la view affichant la recette choisi
def recette_detail_view(request, primary_key):
    # On essaie d'exécuter la commande ce trouvant après le try
    try:
        # On recherche dans la table Recette si un enregistrement possède bien l'identifiant récupéré
        recette = Recette.objects.get(pk=primary_key)
    # Dans le cas ou l'identifiant n'existe pas
    except Recette.DoesNotExist:
        # Alors on affiche une erreur 404 et on arrête l'exécution s'arrête ici
        raise Http404('Recette inexistante')
	# Si aucun erreur, on renvoi la recette au template recette_detail.html
    return render(request, 'recettes/recette_detail.html', context={'recette': recette})

# Affichage des commentaires comme pour les recettes
def commentaires(request):
    comment = Comment.objects.all
    return render(request, 'comment/comment.html', {'comment': comment})

# View récupérant les informations envoyés par l'utilisateur
def comment(request):
    error = False
    # Si une requête POST à eu lieu
    if request.POST:
        # Si le pseudo est bien existant
        if 'pseudo' in request.POST:
            name = request.POST.get('pseudo', '')
        else:
            error = True
        # Si le commentaire est bien existant
        if 'comment' in request.POST:
            message = request.POST.get('comment', '')
        else:
            error = True
        # Pas d'erreur, nous pouvons l'enregistrer en base de données
        if not error:
            # Insertion des données depuis le modèle
            new_comment = Comment(pseudo=name, comment=message)
            # Enregistrement en base de donnée
            new_comment.save()
            # redirection vers la view commentaire
            return commentaires(request)
        else:
            return HttpResponse("An error has occured")
    else:
        return commentaires(request)