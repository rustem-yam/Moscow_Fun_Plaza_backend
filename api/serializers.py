from rest_framework import serializers
from .models import Event, EventTag, EventType


class EventTagSerializer(serializers.ModelSerializer):
  class Meta:
    model = EventTag
    fields = ('name',)


class EventTypeSerializer(serializers.ModelSerializer):
  class Meta:
    model = EventType
    fields = ('name',) 


class EventSerializer(serializers.ModelSerializer):
  tags = EventTagSerializer(read_only=True, many=True)
  type = EventTypeSerializer(read_only=True)
  class Meta:
    model = Event
    fields = ('name', 'description', 'date', 'ticket_price', 'address', 'likes', 'tags', 'type')



