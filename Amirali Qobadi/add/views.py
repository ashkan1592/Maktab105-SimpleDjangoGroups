from pyexpat.errors import messages

from django.http import HttpResponseRedirect
from django.shortcuts import render
from . import forms
from .forms import AddForm
from .models import Add


# Create your views here.
def add(request):
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            music_info = form.cleaned_data
            Add.objects.create(name=music_info['name'], cover=music_info['cover'], category=music_info['category'],
                               url=music_info['url'])
            return HttpResponseRedirect('/')


    else:
        form = AddForm()
        return render(request, 'add.html', {'form': form})
