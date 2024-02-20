from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
# from django.http import HttpResponse
from music.models import Song, Category
from .forms import AddSongForm
from django.contrib import messages


# Create your views here.


class SongListView(View):
    def get(self, request):
        songs = Song.objects.all()
        return render(request, 'home.html', {'songs': songs})


class SongDetailView(View):
    def get(self, request, pk):
        song = get_object_or_404(Song, pk=pk)
        return render(request, 'detail.html', context={'song': song})


# class AddSongView(View):
#     def get(self, request):
#         form = AddForm()
#         return render(request, 'add_song.html', context={'form': form})
#
#     def post(self, request):
#         form = AddForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             # new_song = Song.objects.create(name=cd['name'], cover=cd['cover'], url=cd['url'], category=cd['category'])
#             new_song = Song(name=cd['name'], cover=cd['cover'], url=cd['url'])
#             messages.success(request, 'New song added!')
#             return redirect('song_detail', pk=new_song.pk)
#         else:
#             messages.error(request, 'Invalid data!')
#             return render(request, 'add_song.html', context={'form': form})
#
#
class DeleteSongView(View):
    def get(self, request, pk):

        if isinstance(pk, int):
            song = get_object_or_404(Song, pk=pk)
            print(song.pk)
        else:
            song = get_object_or_404(Song, name=pk)
        return render(request, 'delete.html', {'song': song})

    def post(self, request, pk):
        if isinstance(pk, int):
            song = get_object_or_404(Song, pk=pk)
        else:
            song = get_object_or_404(Song, name=pk)
        song.delete()
        return redirect('song_list')


class AddSongView(View):
    def get(self, request):
        form = AddSongForm()
        return render(request, 'add_song.html', {'form': form})

    def post(self, request):
        form = AddSongForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            cover = form.cleaned_data['cover']
            url = form.cleaned_data['url']
            category_name = form.cleaned_data['category_name']

            # Check if category exists
            category, created = Category.objects.get_or_create(category=category_name)

            # Create the song
            song = Song.objects.create(name=name, cover=cover, url=url, category=category)
            return redirect('song_detail', pk=song.pk)

        return render(request, 'add_song.html', {'form': form})


class SongInfoView(View):
    def get(self, request):
        song_count = Song.objects.count()
        category_count = Category.objects.count()
        category_counts = {}
        for category in Category.objects.all():
            category_counts[category.category] = Song.objects.filter(category=category).count()

        return render(request, 'info.html',
                      {
                          'song_count': song_count,
                          'category_count': category_count,
                          'category_counts': category_counts
                      })
