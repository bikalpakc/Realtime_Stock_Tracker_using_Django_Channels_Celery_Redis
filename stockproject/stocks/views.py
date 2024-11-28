from django.shortcuts import render
import requests
# Create your views here.

def stocktracker(request):    
    return render(request, 'stocktracker.html',)