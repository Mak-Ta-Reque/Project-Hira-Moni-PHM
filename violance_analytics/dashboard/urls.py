from django.urls import path
from . import views
from .views import CityCharView, ListCity, open_dashboard
from .dash_apps.finished_apps import simpleexample


urlpatterns = [
    path('', open_dashboard, name='dashboard'),
]
