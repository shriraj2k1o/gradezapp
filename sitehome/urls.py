from django.urls import path
from . import views

app_name = 'sitehome'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('get-started', views.getStarted, name = 'getStarted'),
    path('login/', views.login, name = 'login'),
    path('logout/', views.logout, name = 'logout')
]