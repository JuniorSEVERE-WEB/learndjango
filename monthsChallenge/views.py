from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.

dict_months = {
    "january": " We are in january",
    "februray": " We are in february",
    "march": "We are in march",
    "april": "We are in april",
    "may": "We are in may",
    "june": "We are in june",
    "july": "We are in july",
    "august": "We are in august",
    "september": "We are in september",
    "october": "We are in october",
    "november": "We are in november",
    "december": "we are in december"
}

def index(request):
    return HttpResponse("Welcome to the challenge of the all months!")

def months_by_int(request, month):
    return HttpResponse(month)
    
def months_by_str(request, month):
    try:
        message_month = dict_months[month]
        return HttpResponse(message_month)
    except:
        return HttpResponseNotFound("Invalid month!")