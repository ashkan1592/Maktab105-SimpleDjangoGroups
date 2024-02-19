from django.urls import path
from . import views

urlpatterns = [
    path('', views.SongListView.as_view(), name='song_list'),
    path('<int:pk>/', views.SongDetailView.as_view(), name='song_detail'),
    path('add/', views.AddSongView.as_view(), name='add_song'),
    path('delete/<int:pk>/', views.DeleteSongView.as_view(), name='delete_song'),
    path('delete/<str:pk>/', views.DeleteSongView.as_view(), name='delete_song'),
    path('info/', views.SongInfoView.as_view(), name='info')
]
