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


# class DeleteMusicView(DeleteView):
#     model = MusicModel
#     template_name = 'Musics/delete.html'
#     success_url = reverse_lazy('info')
#     success_message = "Music deleted successfully"
#     error_message = "Error deleting music"
#     context_object_name = 'music'
#     pk_url_kwarg = 'pk'

# def delete(self, request, *args, **kwargs):
#     self.object = self.get_object()
#     success_url = self.get_success_url()
#     try:
#         self.object.delete()
#         messages.success(request, "Music deleted successfully")  # Display success message
#     except Exception as e:
#         messages.error(request, "Error deleting music: {}".format(str(e)))  # Display error message
#     return HttpResponseRedirect(success_url)


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


#
# class CountMusicView(DetailView):
#     model = MusicModel
#     template_name = 'Musics/info.html'
#     context_object_name = 'music'
#     # pk_url_kwarg = 'pk'
# class CountMusicView(ListView):
#     model = MusicModel
#     template_name = 'Musics/count.html'
#     context_object_name = 'music'
#     success_message = "Music added successfully"
#     error_message = "Error adding music"
#     # pk_url_kwarg = 'pk'
#     fields = '__all__'
#     queryset = MusicModel.objects.all()
#

class CountMusicView(ListView):
    template_name = 'Musics/count.html'  # Update with your template path
    context_object_name = 'category_counts_data'  # Context variable name in the template

    def get_queryset(self):
        return CategoryModel.objects.annotate(num_albums=Count('Album'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Optionally, you can further customize the context data here
        # For example, you might want to add additional context variables or perform additional queries
        return context
