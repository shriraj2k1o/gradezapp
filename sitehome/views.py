from django.shortcuts import render, redirect
from .models import Users
# from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'sitehome/index.html')


def getStarted(request):
    return render(request, 'sitehome/get-started.html')


def getDemo(request):
    if request.method=='GET':
        email = request.GET['mail']
        password = request.GET['pass']

        user = Users.objects.filter(email=mail)

        if user:
            redirect(request, 'student/index.html')
        else:
            err = "Account doesn't Exist"
        print('Dataposted -->' + mail + password)
    return render(request, 'sitehome/login.html', { 'err' : err})
