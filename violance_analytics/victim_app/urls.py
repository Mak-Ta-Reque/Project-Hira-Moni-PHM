from django.urls import path
from . import views

urlpatterns = [

    path('', views.contact),
    path('application/', views.victim_application_view),
    ]
