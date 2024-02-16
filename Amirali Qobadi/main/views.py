from django.shortcuts import render
from .models import Urls


# Create your views here.


def main_page(request):
    all_urls = Urls.objects.all()
    return render(request, 'main.html', {'all_urls': all_urls})
