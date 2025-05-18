from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name ='student_dashboard'),
    path('milestone/', views.milestone_view, name='milestone'),
    path('milestone/delete/<int:pk>/', views.delete_milestone, name='delete_milestone'),
]
