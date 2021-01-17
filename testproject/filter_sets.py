import django_filters
from taggit.models import Tag

from query_view.filter_sets import FilterSet

from .models import ActorTypedTag
from .models import DirectorTypedTag
from .models import Thing


class ThingFilterSet(FilterSet):
    tags = django_filters.ModelMultipleChoiceFilter(label='Tags', queryset=Tag.objects.all(), conjoined=True)
    not_tags = django_filters.ModelMultipleChoiceFilter(field_name='tags', label='Tags', queryset=Tag.objects.all(), conjoined=True, exclude=True)
    actortaggedthing__typed_tag = django_filters.ModelMultipleChoiceFilter(label='Actor Tags', queryset=ActorTypedTag.objects.all(), conjoined=True)
    not_actortaggedthing__typed_tag = django_filters.ModelMultipleChoiceFilter(field_name='actortaggedthing__typed_tag', label='Actor Tags', queryset=ActorTypedTag.objects.all(), conjoined=True, exclude=True)
    directortaggedthing__typed_tag = django_filters.ModelMultipleChoiceFilter(label='Director Tags', queryset=DirectorTypedTag.objects.all(), conjoined=True)
    not_directortaggedthing__typed_tag = django_filters.ModelMultipleChoiceFilter(field_name='directortaggedthing__typed_tag', label='Director Tags', queryset=DirectorTypedTag.objects.all(), conjoined=True, exclude=True)
    layout_fields = ['name__icontains']

    class Meta:
        model = Thing
        fields = {
            'name': ['icontains'],
            'is_good': ['exact'],
        }
