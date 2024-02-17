from django.contrib import admin

# Register your models here.
from music.models import Category, Music

admin.site.register((Category, Music))
