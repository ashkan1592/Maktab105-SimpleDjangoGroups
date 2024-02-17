from django.contrib import admin
from .models import Music  # Assuming Music is defined in your models.py

class MusicAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'url', 'cover', 'category']

admin.site.register(Music, MusicAdmin)