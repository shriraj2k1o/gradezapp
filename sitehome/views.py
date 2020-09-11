from django.shortcuts import render, redirect
from .models import Users
# from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'sitehome/index.html')


def getStarted(request):
    return render(request, 'sitehome/get-started.html')


def getDemo(request):
    
    return render(request, 'sitehome/login.html')