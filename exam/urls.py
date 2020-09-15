from django.urls import path
from . import views

app_name = 'exam'

urlpatterns = [
    path('add-question/', views.AddQuestion , name = "addQuestion")
]