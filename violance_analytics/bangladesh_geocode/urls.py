from django.conf.urls import url
from django.urls import path

from . import views, db_manager

urlpatterns = [
    path('', views.initialize, name='init'),
]



#db_manager.populate_database()
