from django.http import HttpResponse
from django.shortcuts import render
from .db_manager import populate_database


# Create your views here.
def initialize(request):
    populate_database()

    return HttpResponse(status=201)
