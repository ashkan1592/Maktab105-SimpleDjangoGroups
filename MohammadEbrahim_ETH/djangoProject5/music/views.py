from django.views.generic import ListView, DeleteView, CreateView
from django.shortcuts import HttpResponse, get_object_or_404
from music.models import Music, Category
from music.forms import MusicForm


class MusicListView(ListView):
    model = Music
    template_name = 'index.html'


class MusicDeleteView(DeleteView):
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

    def get_queryset(self):
        queryset = super().get_queryset()
        categories = Category.objects.all()
        reports = []
        for category in categories:
            report = {
                'category': category.name,
                'songs_count': Music.objects.filter(category=category).count()
            }
            reports.append(report)
        return reports


class MusicAddView(CreateView):
    model = Music
    form_class = MusicForm
    template_name = 'add.html'
