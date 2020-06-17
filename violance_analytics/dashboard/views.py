from django.shortcuts import render
from django.views.generic import TemplateView
from .models import City

def home(request):
    return render(request, 'index.html')


class CityCharView(TemplateView):
    template_name = 'cities/chart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"] = City.objects.all()
        return context

