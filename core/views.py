from django.shortcuts import redirect, render
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'home.html')

@login_required
def role_redirect(request):
    email = request.user.email
    if email.endswith('@student.uitm.edu.my'):
        return redirect('student_dashboard')
    elif email.endswith('@gmail.com'):
        return redirect('lecturer_dashboard')
    else:
        return redirect('home')
    
def logout_view(request):
    logout(request)
    return redirect('https://accounts.google.com/Logout?continue=https://appengine.google.com/_ah/logout?continue=http://127.0.0.1:8000/')