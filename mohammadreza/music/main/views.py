from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView
from django.http import HttpResponse
from .forms import Form, CategoryForm
from .models import Add,Category
from django.contrib import messages
from django.db.models import Count




class CreateCategory(View):
    template_name = 'add_category.html'
    def get(self, request):
        category_form = CategoryForm()
        return render(request, self.template_name, {"category_form": category_form})

    def post(self, request):
        category_form=CategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            messages.success(request, "category add Successfully")
            return redirect('category')
        else:
            category_form = CategoryForm()
            return render(request,self.template_name,{"category_form":category_form})


class AddView(View):
    template_name = 'add_music.html'

    def get(self, request):
        form = Form()
        return render(request, self.template_name, {"form": form})




    def post(self, request):
            form=Form(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "music add Successfully")
                return redirect('add')
            else:
                form = Form()
                return render(request,self.template_name,{"form":form})


class Display(View):
    te = 'display_musics.html'
    def get(self,request):
        all_musics=Add.objects.all()
        return render(request,self.te,{"all_musics":all_musics})


class Delete(View):
    def get(self,request,id):
        delete_music=Add.objects.get(id=id)
        delete_music.is_delete=True
        delete_music.save()
        messages.success(request, f"{delete_music.name} music delete Successfully")
        return redirect('display')

class Detail(View):
    def get(self, request, id):
        detail_music = Add.objects.get(id=id)
        return render(request, "music_detail.html", {'detail_music': detail_music})


class Info(View):
    def get(self, request):
        info = Add.objects.all()
        count_info = {
            'total_music_count': info.count(),
            'total_category_count': info.values('category').distinct().count(),
            'category_with_post_count' :Category.objects.annotate(post_count=Count('add'))
        }
        return render(request, "music_info.html", {'count_info': count_info, "info":info})

