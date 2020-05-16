from django.urls import path
from . import views

app_name = 'sitehome'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('get-started', views.getStarted, name = 'getStarted'),
    path('get-demo', views.getDemo, name = 'getDemo')
]