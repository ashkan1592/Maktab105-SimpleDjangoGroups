from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from .forms import MusicForm
from .models import Music
from django.urls import reverse_lazy
from django.db.models import Count   # Add this import

class HomeView(ListView):
    model = Music
    template_name = 'home.html'
    context_object_name = 'musics'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Music.objects.all()
        return context

class AddMusicView(CreateView):
    template_name = 'add.html'
    model = Music
    fields = '__all__'
    success_url = reverse_lazy('home')

class DeleteMusicView(DeleteView):
    def get(self, request, *args, **kwargs):

        identifier = kwargs.get('identifier')

        if identifier.isdigit():
            music = get_object_or_404(Music, id=identifier)
        else:
            music = get_object_or_404(Music, name=identifier)

        music.delete()

        return HttpResponse("Music deleted successfully", status=200)

class MusicInfoView(ListView):
    model = Music
    template_name = 'info.html'
    context_object_name = 'music_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_songs'] = Music.objects.count()
        context['categories'] = Music.objects.values('category').distinct().annotate(total_songs=Count('id'))
        context['total_categories'] = len(context['categories'])
        return context
