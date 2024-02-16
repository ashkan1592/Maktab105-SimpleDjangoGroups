from django.shortcuts import render , get_object_or_404, redirect
from django.views import View
from .forms import InputForm
from .models import Musics
from django.urls import reverse
from django.db.models import Count



class MusicAdd(View):
    # form_class=InputForm
    template_name = "add.html"

    def get(self , request , *args , **kwargs):
         return (form := InputForm()) and render(request, self.template_name, {'form': form})
    
    def post(self , request , *args , **kwargs):
        form =InputForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('music_list'))
        else:
            return render(request, self.template_name, {"form" : form} )



class MusicList(View):
     def get(self, request):
        music_list = Musics.objects.all()
        return render(request, 'music_list.html', {'music_list': music_list})

    

class MusicInfo(View):
    def get(self, request):
        total_songs = Musics.objects.count()
        categories_count = Musics.objects.values('category').annotate(count_songs=Count('category'))

        

        category_counts = {}
        for category in categories_count:
            category_name = category['category']
            count = category['count_songs']
            category_counts[category_name] = count
        
        return render(request, 'info.html', {'total_songs': total_songs, 'categories_count': len(categories_count), 'category_counts': category_counts})

class MusicDelete(View):
    pass

