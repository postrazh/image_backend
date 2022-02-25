from django.urls import path, re_path
from django.views.generic import RedirectView

from api.views import CarListView

urlpatterns = [
    path('', RedirectView.as_view(url='cars/', permanent=False)),
    re_path('cars/$', CarListView.as_view()),
    re_path('cars/(?P<platform>.+)/$', CarListView.as_view()),
]
