from django.contrib.auth import get_user_model
from rest_framework import serializers

from ..models.stretch import Stretch

class StretchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stretch
        fields = ('id', 'name', 'description', 'video', 'instructions', 'owner')
