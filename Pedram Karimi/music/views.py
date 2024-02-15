from django.contrib import messages
from django.views.generic import CreateView, ListView, View
from django.shortcuts import get_object_or_404, redirect
from django.db.models import Count
from django.urls import reverse_lazy
from .models import MusicModel, CategoryModel


class AddMusicView(CreateView):
    model = MusicModel
    fields = '__all__'
    success_url = reverse_lazy('home')
    template_name = 'Musics/add.html'
    context_object_name = 'music'
    success_message = "Music added successfully"
    error_message = "Error adding music"


class InfoMusicView(ListView):
    model = MusicModel
    template_name = 'Musics/info.html'
    context_object_name = 'music'
    success_message = "Music added successfully"
    error_message = "Error adding music"



class DeleteMusicView(View):
    model = MusicModel
    success_url = reverse_lazy('info')

    def get(self, request, pk):
        if isinstance(pk, int):
            (music := get_object_or_404(self.model, pk=pk)) and music.delete()
        else:
            (music := get_object_or_404(self.model, title=pk)) and music.delete()
        messages.success(request, 'Music deleted successfully', extra_tags='success')
        return redirect('info')



class CountMusicView(ListView):
    template_name = 'Musics/count.html'  
    context_object_name = 'category_counts_data'  

    def get_queryset(self):
        return CategoryModel.objects.annotate(num_albums=Count('Album'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
