from django.contrib import admin

from .models import ActorTypedTag
from .models import DirectorTypedTag
from .models import LanguageTypedTag
from .models import TaggedThing
from .models import Thing

admin.site.register(ActorTypedTag)
admin.site.register(DirectorTypedTag)
admin.site.register(LanguageTypedTag)
admin.site.register(TaggedThing)
admin.site.register(Thing)
