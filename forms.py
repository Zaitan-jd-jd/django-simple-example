from django import forms
from .models import profile

class username_form(forms.Form):
    username = forms.CharField(label='Il tuo nome', max_length=25)
class email_form(forms.Form):
    email = forms.EmailField(label='inserisci la tua email', max_length=40)