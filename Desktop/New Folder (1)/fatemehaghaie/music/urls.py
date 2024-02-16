from django.urls import path
from django.urls import path
from .views import MusicListView, AddMusicView, DeleteMusicView, InfoView
urlpatterns = [
    path('', MusicListView.as_view(), name='music'),
    path('add/', AddMusicView.as_view(), name='add'),
    path('<int:id>/delete/', DeleteMusicView.as_view(), name='delete'),
    path('info/', InfoView.as_view(), name='info'),]

