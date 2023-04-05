from django.views.generic import ListView

from core.models import Women


class HomeTempaltes(ListView):
    model = Women
    template_name = 'home.html'
    context_object_name = 'womens'

    def get_queryset(self):
        return Women.objects.filter(is_published=True).select_related('cat')
