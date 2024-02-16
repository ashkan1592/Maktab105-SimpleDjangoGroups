from django.views.generic import ListView, CreateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from .models import Music
from django.db.models import Count  # Import Count from django.db.models

class MusicListView(ListView):
    model = Music
    template_name = 'music/music_list.html'
    context_object_name = 'musics'

class MusicCreateView(CreateView):
    model = Music
    template_name = 'music/music_form.html'
    fields = ['name', 'category', 'url', 'cover']
    success_url = reverse_lazy('music_list')

class MusicDeleteView(DeleteView):
    model = Music
    success_url = reverse_lazy('music_list')

class MusicReportView(TemplateView):
    template_name = 'music/music_report.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['num_songs'] = Music.objects.count()
        context['categories'] = Music.objects.values('category').annotate(count=Count('category'))  # Use Count from django.db.models
        context['num_categories'] = len(context['categories'])
        return context
