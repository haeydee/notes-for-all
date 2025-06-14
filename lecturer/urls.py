from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.lecturer_dashboard, name='lecturer_dashboard'),
    path('upload-txt/', views.upload_txt, name='upload_txt'),
    path('upload-material/', views.upload_material, name='upload_material'),
    path('materials/', views.material_list, name='material_list'),
    path('class-select/', views.select_classes, name='select_class'),
    path('supervisor-dashboard/', views.supervisor_dashboard, name='supervisor_dashboard'),
    path('approve-request/<int:request_id>/', views.approve_request, name='approve_request'),
]