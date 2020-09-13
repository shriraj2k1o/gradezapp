from django.urls import path,include
from . import views

app_name = 'siteadmin'

urlpatterns = [
    path('', views.AdminDashboard, name = 'index')
]
