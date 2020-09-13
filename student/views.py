from django.shortcuts import render, redirect

# Create your views here.
def StudentDashboard(request):
    email = request.session.get('email')
    if email:
        return render(request, 'student/index.html')
    else:
       
        return redirect('sitehome:login')