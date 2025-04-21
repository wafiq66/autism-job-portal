from django.shortcuts import render

# Create your views here.
def landing_page(request):
    if request.user.is_authenticated:
        context = {
            'user': request.user,
            'show_personal': True
        }
    else:
        context = {
            'show_personal': False
        }
    return render(request, 'search_job.html', context)