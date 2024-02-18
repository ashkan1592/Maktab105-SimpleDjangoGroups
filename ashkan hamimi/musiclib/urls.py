from django.urls import path
from .views import (
    add_music,
    add_category,
    music_with_categories,
    info,
    music_list,
    music_detail,
    delete_music,
)

urlpatterns = [
    path("addmusic/", add_music, name="add_music"),
    path("addcategory/", add_category, name="add_category"),
    path("", music_with_categories, name="music_with_categories"),
    path("info/", info, name="info"),
    path("list/", music_list, name="music_list"),
    path("<int:music_id>/", music_detail, name="music_detail"),
    path("<int:music_id>/delete/", delete_music, name="delete_music"),
]
