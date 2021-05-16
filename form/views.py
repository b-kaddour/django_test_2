from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ContactForm

def contact(request):
    # si c'est une demande POST, nous devons traiter les données du formulaire.
    if request.method == 'POST':
        # créer une instance de formulaire et la remplir avec les données de la requête
        form = ContactForm(request.POST)
        # On checke si c'est valide
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # On redirige vers la page
            return HttpResponseRedirect('//')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm()
    return render(request, 'form/contact.html', {'form': form})

def merci(request):
    return render(request, 'form/merci.html', {})