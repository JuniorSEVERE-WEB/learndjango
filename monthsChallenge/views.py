from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.

def index(request):
    return HttpResponse("Welcome to the challenge of the all months!")

def months(request, month):
    if month == "january":
        message_month = "We are in january, we ate rice"
    elif month == "february":
        message_month = "We are in february"
    else:
        return HttpResponseNotFound("Invalid month!")     
    return HttpResponse(message_month)