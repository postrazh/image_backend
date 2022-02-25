from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from api.models import Car


class CarSerializer(ModelSerializer):
    image_web = serializers.ImageField(read_only=True)
    image_mobile = serializers.ImageField(read_only=True)

    class Meta:
        model = Car
        fields = ['id', 'title', 'description', 'image_file', 'image_web', 'image_mobile']
