from django.shortcuts import render
from django.db.models import Sum
from django.http import JsonResponse
from django.http import HttpResponseRedirect, HttpResponse


def home(request):
    return render(request, 'index.html')



