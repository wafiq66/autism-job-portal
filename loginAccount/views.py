from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def login_applicant(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request,username=email,password=password)
        
        if user is not None:
            login(request,user)
            return redirect('landing_page')
        else:
            messages.error(request, 'Invalid email or password!')
            return redirect('login_applicant')

    return render(request, 'login_applicant.html')

def logout_application(request):
    logout(request)
    return redirect('landing_page')