from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')

def login_view(request):
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    google_logout_url = (
        "https://accounts.google.com/Logout"
        "?continue=https://appengine.google.com/_ah/logout"
        f"?continue={request.build_absolute_uri('/')}"
    )
    return redirect(google_logout_url)

def get_user_role(email):
    if email.endswith('student.uitm.edu.my'):
        return 'student'
    elif email.endswith('uitm.edu.my'):
        return 'lecturer'
    return None

# accessible post login
def login_redirect(request):
    email = request.user.email
    role = get_user_role(email)
    if role == 'lecturer':
        return redirect('lecturer_dashboard')
    elif role == 'student':
        return redirect('student_dashboard')
    else:
        logout(request)
        return render(request, 'access_denied.html')
