from django.shortcuts import render
from datetime import datetime
from django.contrib import admin
from django.http import request
from django.http import HttpResponseRedirect

from .models import profile
from .forms import username_form, email_form

def username(request):
    if request.method == 'POST':
        username = username_form(request.POST)
        if username_form.is_valid(username):
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/home/')
    else:
        username= username_form()
    def __init__(self):
        return self.username()
    context = {'username': username, 'username_form': username_form()}
    return render(request, 'registrati.html', context)

def datetime_profile():
    for datetime_profile in username():
        if username_form().is_valid():
            datetime_profile = username(username).datetime(year, month, day)
        else:
            pass
    context = {'datetime_profile': datetime_profile}
    return render(request, 'registrati.html', context)

def email(email):
    if request.method == 'POST':
        email = email_form(request.POST)
        if email_form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        email = email_form()
    context = {'email': email}
    return render(request, 'registrati.html', context)