from django.urls import path
from .views import (
    AddMusic,
    AddCategory,
    MusicWithCategories,
    Info,
    MusicList,
    MusicDetail,
    MusicDelete,
)

urlpatterns = [
    path("addmusic/", AddMusic.as_view(), name="add_music"),
    path("addcategory/", AddCategory.as_view(), name="add_category"),
    path("", MusicWithCategories.as_view(), name="music_with_categories"),
    path("info/", Info.as_view(), name="info"),
    path("list/", MusicList.as_view(), name="music_list"),
    path("<int:music_id>/", MusicDetail.as_view(), name="music_detail"),
    path("<int:music_id>/delete/", MusicDelete.as_view(), name="delete_music"),
]
