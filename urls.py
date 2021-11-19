from django.urls import path

from . import views

urlpatterns = [
    path('', views.username, name='username'),
    path('', views.datetime_profile, name='datetime_profile'),
    path('', views.email, name='email'),

]