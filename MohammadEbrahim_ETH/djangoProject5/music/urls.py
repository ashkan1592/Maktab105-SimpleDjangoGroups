from django.urls import path
from music.views import MusicAddView, MusicDeleteView, MusicInfoView, MusicListView

urlpatterns = [
    path('', MusicListView.as_view(), name='index'),
    path('add/', MusicAddView.as_view(), name='add'),
    path('delete/<str:identifier>/', MusicDeleteView.as_view(), name='delete'),
    path('info/', MusicInfoView.as_view(), name='info'),
]
