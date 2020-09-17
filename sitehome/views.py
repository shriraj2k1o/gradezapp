from django.shortcuts import render, redirect
from .models import Users
from .forms import LoginForm
# from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'sitehome/index.html')


def getStarted(request):
    return render(request, 'sitehome/get-started.html')


def login(request):
    err = ""
    if request.method == 'POST':
        # creates form instance
        form = LoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['user_email']
            password = form.cleaned_data['user_password']

            get_user = Users.objects.filter(email=email)
            
            if not get_user:
                err = "User doesn't exist"
                print("no user")
            else:
                user = get_user[0]
                # for user in get_user:
                if password == user.password:

                    if user.profession == 'S':
                        # session
                        
                        request.session['email'] = email
                        request.session['profession'] = 'S'
                        request.session['name'] = user.name
                        return redirect('student:index')
                    elif user.profession == 'P':
                        # session
                        request.session['email'] = email
                        request.session['profession'] = 'P'
                        request.session['name'] = user.name
                        return redirect('professor:index')
                    elif user.profession == 'A':
                        # session
                        request.session['email'] = email
                        request.session['profession'] = 'A'
                        request.session['name'] = user.name
                        return redirect('siteadmin:index')
                else:
                    err = "Password wrong"
   
    else:
        form = LoginForm()

    return render(request, 'sitehome/login.html', {'form':form, 'err':err})


def logout(request):
    please_login = "Please login again"

    request.session.flush()

    return redirect('sitehome:login')