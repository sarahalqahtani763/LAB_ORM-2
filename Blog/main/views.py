from django.shortcuts import render
from django.http import HttpRequest ,HttpResponse


# Create your views here.


def home_page_view (request : HttpRequest):
    
    return render(request,"main/home_page.html")