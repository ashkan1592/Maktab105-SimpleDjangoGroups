from django.urls import path
from .views import HomeView, AddMusicView, DeleteMusicView, MusicInfoView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('add/', AddMusicView.as_view(), name='add_music'),
    path('delete/<str:identifier>/', DeleteMusicView.as_view(), name='delete_music'),
    path('info/', MusicInfoView.as_view(), name='music_info'),  # New URL pattern
    # Other URL patterns...
]
