from django.test import TestCase

# Create your tests here.
urlpatterns = [
    path('', views.home, name='home'),
    path('population-chart/', views.population_chart, name='population-chart'),
]