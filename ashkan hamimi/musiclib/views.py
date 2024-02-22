from django.shortcuts import redirect
from django.views.generic import CreateView, ListView, DetailView, DeleteView
from django.urls import reverse_lazy
from .forms import MusicForm, CategoryForm
from .models import Music, Category


class AddMusic(CreateView):
    model = Music
    form_class = MusicForm
    template_name = "add_music.html"
    success_url = reverse_lazy("add_music")


class AddCategory(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = "add_category.html"
    success_url = reverse_lazy("add_category")


class MusicWithCategories(ListView):
    model = Music
    template_name = "music_with_categories.html"
    queryset = Music.objects.prefetch_related("categories").all()
    context_object_name = "music_with_categories"


class Info(ListView):
    template_name = "info.html"
    queryset = Category.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_music"] = Music.objects.count()
        context["music_in_categories"] = {
            category.name: category.music_set.count() for category in self.object_list
        }
        context["total_categories"] = self.object_list.count()
        return context


class MusicList(ListView):
    model = Music
    template_name = "music_list.html"
    context_object_name = "all_music"


class MusicDetail(DetailView):
    model = Music
    template_name = "music_detail.html"
    context_object_name = "music"


class MusicDelete(DeleteView):
    model = Music
    success_url = reverse_lazy("music_list")
    template_name = "music_confirm_delete.html"
