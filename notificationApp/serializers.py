from rest_framework import serializers
from .models import Notification  # Correct model import

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification  # Correct model usage
        fields = [ 'id', 'description', 'created_date']