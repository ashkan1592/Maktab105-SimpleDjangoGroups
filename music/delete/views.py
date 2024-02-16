from django.db.models import Count
from django.views.generic import TemplateView
from add.models import Add
from django.http import HttpResponseNotFound, HttpResponse
from django.shortcuts import get_object_or_404


class DeleteView(TemplateView):
    template_name = "delete.html"

    def get(self, request, music_id_or_name):
        deletion_successful = False
        musics = Add.objects.all()
        for music in musics:
            if music.id == int(music_id_or_name):
                record = Add.objects.get(id=music_id_or_name)
                record.delete()
                deletion_successful = True
        if deletion_successful:
            return HttpResponse(status=200)
        else:
            return HttpResponseNotFound(status=404)
