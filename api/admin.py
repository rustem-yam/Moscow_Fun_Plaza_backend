from django.contrib import admin
from .models import Event, EventTag, EventType

# Register your models here.
admin.site.register(Event)
admin.site.register(EventTag)
admin.site.register(EventType)