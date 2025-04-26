from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Welcome to the challenge of the all months!")

def january(request):
    return HttpResponse("We are in january")