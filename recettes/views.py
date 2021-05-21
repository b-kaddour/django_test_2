from django.shortcuts import render
from django.http import HttpResponse, Http404

from .models import Recette
from .models import Comment


# Create your views here.
def index(request):
    recette = Recette.objects.all
    return render(request, 'recettes/index.html', {'recette': recette})


def recette_detail_view(request, primary_key):
    try:
        recette = Recette.objects.get(pk=primary_key)
    except Recette.DoesNotExist:
        raise Http404('Recette inexistante')

    return render(request, 'recettes/recette_detail.html', context={'recette': recette})


def commentaires(request):
    comment = Comment.objects.all
    return render(request, 'comment/comment.html', {'comment': comment})


def comment(request):
    error = False
    if request.POST:
        if 'pseudo' in request.POST:
            name = request.POST.get('pseudo', '')
        else:
            error = True
        if 'comment' in request.POST:
            message = request.POST.get('comment', '')
        else:
            error = True
        if not error:
            new_comment = Comment(pseudo=name, comment=message)
            new_comment.save()
            return commentaires(request)
        else:
            return HttpResponse("An error has occured")
    else:
        return commentaires(request)
