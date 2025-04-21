from django.shortcuts import render, redirect
from appUser.models import app_user
from django.contrib import messages

# Create your views here.
def register_applicant(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        first_name = request.POST.get('first-name')
        last_name = request.POST.get('last-name')
        password1 = request.POST.get('password')
        password2 = request.POST.get('confirm-password')
        # Check if the two passwords arent match
        if password1 != password2:
            messages.error(request,"Password do not match!")
            return redirect('register_applicant')
        
        if app_user.objects.filter(username=email).exists():
            messages.error(request, 'Email already registered.')
            return redirect('register_applicant')
        
        applicant = app_user.objects.create_user(
            username=email,
            email=email,
            password=password1, 
            first_name=first_name, 
            last_name=last_name)
        
        messages.success(request,"Applicant Successfully Registered!")
        return redirect('register_applicant')
    return render(request,"applicant_register.html")