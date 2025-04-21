from django.urls import path
from . import views

urlpatterns=[
    path('applicant/',views.login_applicant,name='login_applicant'),
    path('logout/applicant',views.logout_application,name='logout_applicant'),
]