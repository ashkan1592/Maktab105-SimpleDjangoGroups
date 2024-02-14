from django.urls import path
from .views import MusicListView, MusicCreateView, MusicDeleteView, MusicReportView

urlpatterns = [
    path('', MusicListView.as_view(), name='music_list'),
    path('add/', MusicCreateView.as_view(), name='music_create'),
    path('delete/<int:pk>/', MusicDeleteView.as_view(), name='music_delete'),
    path('info/', MusicReportView.as_view(), name='music_report'),
]
