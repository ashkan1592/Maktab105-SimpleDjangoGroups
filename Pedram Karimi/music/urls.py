from django.urls import path
from .views import AddMusicView, CountMusicView, DeleteMusicByIDView, InfoMusicView, DeleteMusicByNameView

urlpatterns = [
    path('', InfoMusicView.as_view(), name='home'),
    path('add/', AddMusicView.as_view(), name='add'),
    path('info/', CountMusicView.as_view(), name='info'),
    path('delete/<uuid:pk>/', DeleteMusicByIDView.as_view(), name='delete'),
    path('delete/<str:pk>/', DeleteMusicByNameView.as_view(), name='delete'),
]
