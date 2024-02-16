from django.urls import path
from info.views import InfoView

urlpatterns = [
    path('info/', InfoView.as_view(template_name='info.html'), name='info'),
]