from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hi, I am Munish Tanwar. This is my first Django App.")
