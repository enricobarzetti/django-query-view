from django.db import models
from taggit.managers import TaggableManager
from taggit.models import TaggedItemBase
from query_view.models import TypedTag
from query_view.models import make_typed_tag_tagged_model


class TaggedThing(TaggedItemBase):
    content_object = models.ForeignKey('Thing', on_delete=models.CASCADE)


class Thing(models.Model):
    name = models.CharField(max_length=200)
    is_good = models.BooleanField()

    tags = TaggableManager(through=TaggedThing, blank=True)

    def __str__(self):
        return self.name


class LanguageTypedTag(TypedTag):
    pass


LanguageTaggedThing = make_typed_tag_tagged_model('LanguageTaggedThing', LanguageTypedTag, Thing, app_label='testproject')


class DirectorTypedTag(TypedTag):
    pass


DirectorTaggedThing = make_typed_tag_tagged_model('DirectorTaggedThing', DirectorTypedTag, Thing, app_label='testproject')


class ActorTypedTag(TypedTag):
    pass


ActorTaggedThing = make_typed_tag_tagged_model('ActorTaggedThing', ActorTypedTag, Thing, app_label='testproject')
