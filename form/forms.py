from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Nom', max_length=200)
    firstname = forms.CharField(label='Prénom', max_length=200)
    email = forms.EmailField(label='Email', max_length=200)
    message = forms.CharField(label='Message', max_length=1000)