from django.urls import path
from .views import AddMusicView, HomeView, DeleteMusicView, InfoView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('add/', AddMusicView.as_view(), name='add_music'),
    path('info/', InfoView.as_view(), name='info'),
    path('delete/<pk>/', DeleteMusicView.as_view(), name='delete_music')
]