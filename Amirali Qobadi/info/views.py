from django.db.models import Count
from django.views.generic import TemplateView
from add.models import Add


class InfoView(TemplateView):
    template_name = "info.html"

    def get_context_data(self, *args, **kwargs):
        context = super(InfoView, self).get_context_data(**kwargs)
        context['musics'] = Add.objects.count()
        context['category_count'] = Add.objects.values('category').distinct().count()
        music_count_by_category = Add.objects.values('category').annotate(count=Count('category'))
        context['music_count_by_category'] = music_count_by_category
        return context
