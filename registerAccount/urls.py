# jobs/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('account/', views.register_applicant, name='register_applicant'),
]
