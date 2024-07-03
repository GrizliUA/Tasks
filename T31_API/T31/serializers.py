from rest_framework import serializers
from .models import Click


# Serializer for the Restaurant model
class ClickSerializer(serializers.ModelSerializer):
    class Meta:
      model = Click
      fields = '__all__'