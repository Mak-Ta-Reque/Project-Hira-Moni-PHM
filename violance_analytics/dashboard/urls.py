from django.urls import path
from . import views

from .views import CityCharView, ListCity, open_dashboard



urlpatterns = [
    path('', open_dashboard, name='dashboard'),
    path('chart', CityCharView.as_view(), name='chart'),

]
