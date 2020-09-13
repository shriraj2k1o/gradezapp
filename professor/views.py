from django.shortcuts import render, redirect

# Create your views here.
def ProfessorDashboard(request):
    email = request.session.get('email')
    if email:
        return render(request, 'professor/index.html')
    else:
       
        return redirect('sitehome:login')