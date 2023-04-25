from django.contrib import admin

from .models import Retro,Profile,RetroNote,User

# Register your models here.

admin.site.register(Retro)
admin.site.register(Profile)
admin.site.register(RetroNote)