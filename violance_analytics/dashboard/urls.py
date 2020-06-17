from django.urls import path
from . import views, admin

urlpatterns = [
    path('', views.home, name='home'),
    #path('population-chart/', views.population_chart, name='population-chart'),
    #path('pie-chart/', views.pie_chart, name='pie-chart'),
    #path("create/", views.create, name="create"),
    #path("<int:id>", views.index, name="create"),
]
