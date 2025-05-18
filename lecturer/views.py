from django.shortcuts import render, redirect
from social_django.models import UserSocialAuth

def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'lecturer_dashboard.html')
    else:
        return redirect('login')
    


