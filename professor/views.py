from django.shortcuts import render, redirect

# Create your views here.
def ProfessorDashboard(request):
    email = request.session.get('email')
    name = request.session.get('name')
    profession = request.session.get('profession')
    if email:
        if profession == 'P':
            return render(request, 'professor/index.html', {'name':name})
        elif profession == 'S':
            return redirect('student:index')
        elif profession == 'A':
            return redirect('siteadmin:index')
    else:
       
        return redirect('sitehome:login')