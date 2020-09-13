from django.shortcuts import render, redirect

# Create your views here.
def AdminDashboard(request):
    email = request.session.get('email')
    if email:
        return render(request, 'siteadmin/index.html')
    else:
       
        return redirect('sitehome:login')