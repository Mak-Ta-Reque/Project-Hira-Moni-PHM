from django.shortcuts import render
from django.db.models import Sum
from django.http import JsonResponse
from .models import City, Country
from .forms import CreateNewList
from django.http import HttpResponseRedirect, HttpResponse

def home(request):
    return render(request, 'home.html')


def population_chart(request):
    labels = []
    data = []

    queryset = City.objects.values('name').annotate(country_population=Sum('population')).order_by(
        '-country_population')
    for entry in queryset:
        labels.append(entry['country__name'])
        data.append(entry['country_population'])

    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })


def pie_chart(request):
    labels = []
    data = []

    queryset = City.objects.order_by('-population')[:5]
    for city in queryset:
        labels.append(city.name)
        data.append(city.population)

    return render(request, 'pie_chart.html', {
        'labels': labels,
        'data': data,
    })


def index(response, id):
    ls = Country.objects.get(id=id)
    print(ls)
    return HttpResponse("<h1>%s</h1>" % ls.name)


def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)
        if form.is_valid():
            n = form.cleaned_data['name']
            print(n)
            t = Country(name=n)
            t.save()
        return HttpResponseRedirect("%i" %t.id)
    else:
        form = CreateNewList()
    return render(response, "create.html", {"form": form})
