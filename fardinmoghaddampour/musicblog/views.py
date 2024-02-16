from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import CreateView, ListView, DeleteView, TemplateView
from django.urls import reverse_lazy
from django.db import models
from django.db.models import Count
from .models import Song, Category

# Create your views here.


class AddMusicView(CreateView):
    model = Song
    fields = ['name', 'url', 'cover', 'category']
    success_url = reverse_lazy('home')
    template_name = 'add_music.html'


class HomeView(ListView):
    model = Song
    template_name = 'home.html'
    context_object_name = 'songs'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context


class DeleteMusicView(DeleteView):
    model = Song
    success_url = reverse_lazy('home')
    template_name = 'song_confirm_delete.html'

    def get_object(self, queryset=None):
        identifier = self.kwargs.get('pk')
        if identifier.isdigit():
            return get_object_or_404(Song, id=identifier)
        else:
            return get_object_or_404(Song, name=identifier)

    def delete(self, request, *args, **kwargs):
        # noinspection PyAttributeOutsideInit
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()

        # Return an HTTP response with status code 200 (OK)
        return HttpResponse("Successfully deleted.", status=200)


class InfoView(TemplateView):
    template_name = 'info.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        num_songs = Song.objects.count()
        print(f"Total number of songs: {num_songs}")

        num_categories = Category.objects.count()
        print(f"Total number of categories: {num_categories}")

        songs_per_category = Category.objects.annotate(num_songs=Count('song'))

        # Just wrote this two line to check query
        # songs_per_category1 = Category.objects.annotate(num_songs=Count('song')).query
        # print(songs_per_category1)
        for category in songs_per_category:
            print(f"Category: {category.name}, Number of Songs: {category.num_songs}")

        context['num_songs'] = num_songs
        context['num_categories'] = num_categories
        context['songs_per_category'] = songs_per_category
        return context
