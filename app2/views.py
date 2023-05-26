from django.shortcuts import render
from django.urls import path
from django.http import HttpResponse

# Create your views here.
def virat(request):
    return HttpResponse('<h1>virat is the best captain</h1>')
