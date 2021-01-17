from query_view.views import QueryView

from .filter_sets import ThingFilterSet
from .models import ActorTypedTag
from .models import DirectorTypedTag


class MyView(QueryView):
    url_name = 'my_view'
    filterset_class = ThingFilterSet
    template_name = 'testproject/my_view.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['actor_tags'] = ActorTypedTag.objects.all()
        context['director_tags'] = DirectorTypedTag.objects.all()
        return context


class MyViewJinja(MyView):
    url_name = 'my_view_jinja'
    filterset_class = ThingFilterSet
    template_name = 'testproject/my_view.jinja'
