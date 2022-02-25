from rest_framework.generics import ListAPIView

from api.models import Car
from api.serializers import CarSerializer


class CarListView(ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def get_serializer_context(self):
        context = super(CarListView, self).get_serializer_context()
        context['platform'] = self.kwargs.get('platform')
        return context
