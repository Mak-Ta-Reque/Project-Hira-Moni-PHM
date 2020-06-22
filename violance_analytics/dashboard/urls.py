from django.urls import path
from . import views

from .views import CityCharView, ListCity


urlpatterns = [
    path('', views.home),
    path('customer', views.customer),
    path('product', views.products),
    path('chart', CityCharView.as_view(), name='chart'),
    path('list', ListCity.as_view(),name='list')

]
