"""
URL configuration for fyp_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('', views.home, name='home'),
    path('redirect/', views.login_redirect, name='login_redirect'),
    path('login/', views.login_view, name='login'),
    path('student/', include('student.urls')),
    path('lecturer/', include('lecturer.urls')),
    path('logout', views.logout_view, name='logout'),
]
