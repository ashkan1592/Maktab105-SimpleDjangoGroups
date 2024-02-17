from django.urls import path
from delete.views import DeleteView

urlpatterns = [
    path('delete/<int:music_id_or_name>/', DeleteView.as_view(template_name='delete.html'), name='delete'),
]
