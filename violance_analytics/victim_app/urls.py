from django.urls import path
from . import views

urlpatterns = [

    path('contact/', views.contact, name='contact'),
    path('application/', views.victim_application_view, name='application'),
    ]