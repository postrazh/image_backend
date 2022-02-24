from rest_framework.generics import ListAPIView

from api.models import Car
from api.serializers import CarSerializer


class CarList(ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
