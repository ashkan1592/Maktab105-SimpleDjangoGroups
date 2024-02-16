from django.shortcuts import render
from add.models import Add


# Create your views here.


def musicview(request):
    my_music = Add.objects.all()
    return render(request, 'musicview.html', {'my_music': my_music})
