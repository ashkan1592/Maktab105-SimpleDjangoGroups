from django.urls import path
from .views import AddMusicView, CountMusicView, DeleteMusicView, InfoMusicView

urlpatterns = [
    path('', InfoMusicView.as_view(), name='home'),
    path('add/', AddMusicView.as_view(), name='add'),
    path('info/', CountMusicView.as_view(), name='info'),
    path('delete/<int:pk>/', DeleteMusicView.as_view(), name='delete'),
    path('delete/<str:pk>/', DeleteMusicView.as_view(), name='delete'),
]
