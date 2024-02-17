from django.urls import path
from . views import MusicAdd , MusicList , MusicDelete , MusicInfo

urlpatterns = [
    path('add/', MusicAdd.as_view(), name='add'),
    path('', MusicList.as_view(), name='music_list'),
    path('info/', MusicInfo.as_view(), name='info'),
    path('delete/<int:music_id>/', MusicDelete.as_view(), name='delete_music_by_id'),
    path('delete/<str:music_name>/', MusicDelete.as_view(), name='delete_music_by_name')
]
    

