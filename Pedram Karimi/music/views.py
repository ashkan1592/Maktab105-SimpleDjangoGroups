from django.contrib import messages
from django.views.generic import CreateView, ListView, DeleteView, TemplateView
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from .models import MusicModel, CategoryModel, AlbumModel
from core.managers import SoftDeleteQuerySet


class AddMusicView(CreateView):
    """
    This view allows users to add new music entries.
    """
    model = MusicModel
    fields = '__all__'
    success_url = reverse_lazy('home')
    template_name = 'Musics/add.html'
    context_object_name = 'music'
    success_message = "Music added successfully"
    error_message = "Error adding music"


class InfoMusicView(ListView):
    """
    This view displays information about existing music entries.
    """
    model = MusicModel
    template_name = 'Musics/info.html'
    context_object_name = 'music'
    success_message = "Music added successfully"
    error_message = "Error adding music"


class DeleteMusicByNameView(DeleteView, SoftDeleteQuerySet):
    """
    A view to delete a music object by its name.
    Inherits from DeleteView and SoftDeleteQuerySet.
    """
    model = MusicModel
    success_url = reverse_lazy('info')
    template_name = 'Musics/delete.html'

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests.
        Deletes the music object(s) with the specified name from the database.
        Adds a success message to inform the user.
        Redirects the user to the success URL.
        """
        MusicModel.objects.filter(name=self.kwargs.get('pk')).delete()
        messages.success(request, 'Music deleted successfully', extra_tags='success')
        return redirect(self.success_url)


class DeleteMusicByIDView(DeleteView, SoftDeleteQuerySet):
    """
    A view to delete a music object by its ID.
    Inherits from DeleteView and SoftDeleteQuerySet.
    """
    model = MusicModel
    success_url = reverse_lazy('info')
    template_name = 'Musics/delete.html'

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests.
        Deletes the music object(s) with the specified ID from the database.
        Adds a success message to inform the user.
        Redirects the user to the success URL.
        """
        MusicModel.objects.filter(id=self.kwargs.get('pk')).delete()
        messages.success(request, 'Music deleted successfully', extra_tags='success')
        return redirect(self.get_success_url())

    def get_object(self, queryset=None):
        """
        Retrieves the music object by its primary key (ID).
        """
        pk = self.kwargs.get('pk')
        return get_object_or_404(self.model, pk=pk)


class CountMusicView(TemplateView):
    """
    This view displays counts of albums, categories, and music entries.
    """
    template_name = 'Musics/count.html'

    def get_context_data(self, **kwargs):
        """
        Add counts of albums, categories, and music entries to the context.
        """
        context = super().get_context_data(**kwargs)
        album_count = AlbumModel.objects.count()
        category_count = CategoryModel.objects.count()
        music_count = MusicModel.objects.count()

        context['album_count'] = album_count
        context['category_count'] = category_count
        context['music_count'] = music_count

        return context
