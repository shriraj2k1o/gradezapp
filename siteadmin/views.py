from django.shortcuts import render, redirect

# Create your views here.
def AdminDashboard(request):
    email = request.session.get('email')
    name = request.session.get('name')
    profession = request.session.get('profession')
    if email:
        if profession == 'A':
            return render(request, 'siteadmin/index.html', {'name':name})
        elif profession == 'S':
            return redirect('student:index')
        elif profession == 'P':
            return redirect('professor:index')
    else:
       
        return redirect('sitehome:login')