from django.shortcuts import render

# Create your views here.
def StudentDashboard(request):
    return render(request, 'student/index.html')