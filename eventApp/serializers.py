from rest_framework import serializers
from .models import Event  # Correct model import

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event  # Correct model usage
        fields = ['id', 'name', 'description', 'created_date']

