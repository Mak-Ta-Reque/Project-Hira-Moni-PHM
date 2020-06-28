from django.urls import path
from . import views

from .views import CityCharView, ListCity


urlpatterns = [
    path('chart', CityCharView.as_view(), name='chart'),

]
