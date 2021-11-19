from django.contrib import admin

from .models import profile

class profileAdmin(admin.ModelAdmin):
    fields = ['datetime_profile', 'email','username']
admin.site.register(profile, profileAdmin)

