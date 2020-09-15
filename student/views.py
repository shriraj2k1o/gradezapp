from django.shortcuts import render, redirect

# Create your views here.
def StudentDashboard(request):
    email = request.session.get('email')
    name = request.session.get('name')
    profession = request.session.get('profession')
    if email:
        if profession == 'S':
            return render(request, 'student/index.html', {'name':name})
        elif profession == 'P':
            return redirect('professor:index')
        elif profession == 'A':
            return redirect('siteadmin:index')
    else:
       
        return redirect('sitehome:login')