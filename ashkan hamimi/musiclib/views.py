from django.shortcuts import render, redirect, get_object_or_404
from .forms import MusicForm, CategoryForm
from .models import Music, Category


def add_music(request):
    if request.method == "POST":
        form = MusicForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("add_music")
    else:
        form = MusicForm()

    return render(request, "add_music.html", {"form": form})


def add_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("add_category")
    else:

        category = CategoryForm()
    return render(request, "add_category.html", {"category": category})


def music_with_categories(request):
    music_with_categories = Music.objects.prefetch_related("categories").all()

    return render(
        request,
        "music_with_categories.html",
        {"music_with_categories": music_with_categories},
    )


def info(request):
    total_music = Music.objects.count()

    music_in_categories = {
        category.name: category.music_set.count() for category in Category.objects.all()
    }

    total_categories = Category.objects.count()

    return render(
        request,
        "info.html",
        {
            "total_music": total_music,
            "music_in_categories": music_in_categories,
            "total_categories": total_categories,
        },
    )


def music_list(request):
    all_music = Music.objects.all()
    print(list(all_music))
    return render(request, "music_list.html", {"all_music": all_music})


def music_detail(request, music_id):
    music = get_object_or_404(Music, pk=music_id)

    return render(request, "music_detail.html", {"music": music})


def delete_music(request, music_id):
    music = get_object_or_404(Music, pk=music_id)

    music.delete()

    return redirect("music_list")
