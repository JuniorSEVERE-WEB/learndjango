from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
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
    list_items = ""
    months = list(dict_months.keys())
    
    for month in months:
        month_path = reverse("months_by_str", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{month.capitalize()}</a></li>"
        
    response_data = f"<ul>{list_items}</ul>"  
    return HttpResponse(response_data)  
        
        
        
   


def months_by_int(request, month):
    months = list(dict_months.keys())
    
    if month > len(months):
        return HttpResponseNotFound("Invalid number! must be between 1 and 12!")
    
    redirect_month = months[month - 1]
    redirect_path = reverse("months_by_str", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)
    
    
def months_by_str(request, month):
    try:
        message_month = dict_months[month]
        return HttpResponse(f"<h1>{message_month}</h1> ")
    except:
        return HttpResponseNotFound("<h1>Invalid month!</h1>")