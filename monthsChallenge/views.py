from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Welcome to the challenge of the all months!")

def months(request, month):
    return HttpResponse(f" We are in {month}")