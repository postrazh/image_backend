from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from api.models import Car

PLATFORM_WEB = 'web'
PLATFORM_MOBILE = 'mobile'
PLATFORMS = [
    PLATFORM_WEB,
    PLATFORM_MOBILE,
]


class CarSerializer(ModelSerializer):
    image = serializers.SerializerMethodField()

    def __init__(self, *args, **kwargs):
        self.platform = kwargs.pop('platform', 'web')
        super().__init__(*args, **kwargs)

    def get_image(self, car: Car):
        request = self.context.get('request')
        platform = self.context.get('platform')

        # This is redundant if there are only 2 platforms, but otherwise this can be useful
        if platform not in PLATFORMS:
            platform = PLATFORM_WEB

        image = car.image_web
        if platform == PLATFORM_MOBILE:
            image = car.image_mobile

        if image:
            return request.build_absolute_uri(image.url)

        return None

    class Meta:
        model = Car
        fields = ['id', 'title', 'description', 'image']
