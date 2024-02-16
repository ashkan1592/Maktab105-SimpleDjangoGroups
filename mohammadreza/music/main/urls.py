
from django.urls import path
from .views import *

urlpatterns = [

    path('category/', CreateCategory.as_view(), name='category'),
    path('add/', AddView.as_view(), name='add'),
    path('delete/<int:id>/', Delete.as_view(), name='delete'),
    path('<int:id>/', Detail.as_view(), name='detail'),
    path('', Display.as_view(), name='display'),
    path('info/', Info.as_view(), name='info')
]