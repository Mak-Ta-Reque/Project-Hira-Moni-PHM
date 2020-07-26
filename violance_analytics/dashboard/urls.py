from django.urls import path
from .views import open_dashboard, contributors
from .dash_apps.finished_apps import simpleexample


urlpatterns = [
    path('', open_dashboard, name='dashboard'),
    path('contributors', contributors, name='contributors')
]
