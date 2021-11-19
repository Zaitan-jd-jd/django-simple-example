from django.db import models
from django.http import request
from datetime import datetime   
# Create your models here.
class profile(models.Model):
    def __str__(profile):
        return profile.username
    username = models.CharField(max_length=25)
    datetime_profile = models.DateTimeField(default=datetime.now())
    email = models.EmailField(max_length=35)