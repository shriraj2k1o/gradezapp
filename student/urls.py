from django.urls import path,include
from . import views

app_name = 'student'

urlpatterns = [
    path('', views.StudentDashboard, name = 'index')
]
