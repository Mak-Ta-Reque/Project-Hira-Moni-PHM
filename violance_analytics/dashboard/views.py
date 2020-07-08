from django.shortcuts import render
from django.views.generic import TemplateView
from .models import City
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from plotly.offline import plot
import plotly.graph_objects as go


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


def open_dashboard(request):
    def scatter():
        x1 = ['Dhaka', 'Sylhet', 'Chittagong', 'Barishal']
        y1 = [30, 35, 10, 45]
        trace = go.Bar(
            x=x1,
            y=y1
        )

        layout = dict(
            xaxis=dict(range=[min(x1), max(x1)]),
            yaxis=dict(range=[min(y1), max(y1)])
        )

        fig = go.Figure(data=[trace], layout=layout)
        fig.update_layout(
            autosize=False,
            width=810,
            height=235,
            margin=dict(
                l=2,
                r=2,
                b=2,
                t=2,
                pad=0
            ),
            paper_bgcolor="LightSteelBlue",
        )
        plot_div = plot(fig, output_type='div', include_plotlyjs=False)
        return plot_div

    context = {
        'plot1': scatter()
    }
    return render(request, 'dashboard.html', context)
