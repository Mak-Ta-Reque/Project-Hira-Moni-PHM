from django.urls import path
from . import views
from dashboard.views import CityCharView
urlpatterns = [
    path('', views.home, name='home'),
    path('chart', CityCharView.as_view(), name='chart')

]
