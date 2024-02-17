from django.shortcuts import render, redirect
from django.views.generic import ListView, View
from .models import Music
from django.db.models import Count
from .forms import Music_Form
from django.http import HttpResponse
class MusicListView(ListView):
    model = Music
    template_name = 'music.html'
class AddMusicView(View):
    def get(self, request):
        form = Music_Form()
        return render(request, 'add.html', {'form': form})
    def post(self, request):
        form = Music_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        return render(request, 'add.html', {'form': form})
class DeleteMusicView(View):
    def get(self, request, id):
        try:
            music = Music.objects.get(id=id)
            music.delete()
            return HttpResponse("successfully!",status=200)
        except Music.DoesNotExist:
            return HttpResponse(status=404)
class InfoView(View):
    def get(self, request):
        total_music = Music.objects.count()
        categories = Music.objects.values('category').annotate(count=Count('category'))
        total_categories = len(categories)
        return render(request, 'info.html',
                      {'total_music': total_music, 'categories': categories, 'total_categories': total_categories})