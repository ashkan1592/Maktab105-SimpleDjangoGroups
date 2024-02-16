from django.contrib import admin
from music.models import AlbumModel, CategoryModel, MusicModel

admin.site.register((AlbumModel, CategoryModel, MusicModel))
