from django.urls import path,include
from . import views

app_name = 'professor'

urlpatterns = [
    path('', views.ProfessorDashboard, name = 'index')
]
