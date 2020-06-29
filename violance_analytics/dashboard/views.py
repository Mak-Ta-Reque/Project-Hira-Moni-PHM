from django.shortcuts import render
from django.views.generic import TemplateView
from .models import City
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required



class CityCharView(TemplateView):
    template_name = 'cities/chart.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"] = City.objects.all()
        return context



class ListCity(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        violence_count = {city.violence for city in City.objects.all()}
        return Response(violence_count)
