from django.contrib import admin

from .models import Retro,Profile,RetroNote,User

# Register your models here.

# admin.site.register(Retro)
admin.site.register(Profile)
admin.site.register(RetroNote)

@admin.register(Retro)
class RetroAdmin(admin.ModelAdmin):
    list_display = ['Sprint_Number','retro_date','position']
    list_filter = ['Sprint_Number','retro_date','position']
    search_fields = ['Sprint_Number','retro_date','position']
    ordering = ['Sprint_Number','retro_date','position']


# @admin.register(RetroNote)
# class RetroNoteAdmin(admin.ModelAdmin):
#     list_display = ['person','retro','vote']
#got error, i cant define multiple admin models 