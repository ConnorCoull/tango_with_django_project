from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says hey there partner! They also said you can see the about page <a href='/rango/about/'>Here</a>")

def about(request):
    return HttpResponse("Rango says here is the about page. <a href='/rango/'>Index</a>")