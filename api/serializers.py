from rest_framework import serializers
from .models import Event


class EventSerializer(serializers.ModelSerializer):
  class Meta:
    model = Event
    fields = ('name', 'date', 'ticket_price', 'address', 'likes')