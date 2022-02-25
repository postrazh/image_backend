from django.urls import path
from django.views.generic import RedirectView

from api.views import CarList

urlpatterns = [
    path('', RedirectView.as_view(url='cars/', permanent=False)),
    path('cars/', CarList.as_view()),
]
