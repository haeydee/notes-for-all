import csv, io
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import LecturerProfile, ClassMaterial
from .forms import LecturerClassForm, ClassMaterialForm
from student.models import StudentProfile

@login_required
def lecturer_dashboard(request):
    LecturerProfile.objects.get_or_create(user=request.user)
    return render(request, 'lecturer/dashboard.html')

def upload_txt(request):
    if request.method == 'POST' and request.FILES.get('txt_file'):
        txt_file = request.FILES['txt_file']

        if not txt_file.name.endswith('.txt'):
            messages.error(request, "Invalid file type. Please upload a .txt file.")
            return redirect('upload_txt')

        data_set = txt_file.read().decode('UTF-8')
        io_string = io.StringIO(data_set)
        created_count = 0

        for line in io_string:
            fields = line.strip().split(',')
            if len(fields) != 5:
                continue  # Skip lines that don't match format

            kumpulan, program, kod_kursus, no_pelajar, nama = [f.strip() for f in fields]

            user, created = User.objects.get_or_create(
                username=no_pelajar,
                defaults={'first_name': nama, 'email': f"{no_pelajar}@example.com"}
            )

            profile, prof_created = StudentProfile.objects.get_or_create(
                user=user,
                defaults={
                    'kumpulan': kumpulan,
                    'program': program,
                    'kod_kursus': kod_kursus,
                    'no_pelajar': no_pelajar,
                    'nama': nama,
                }
            )

            if prof_created:
                created_count += 1

        messages.success(request, f"{created_count} student profiles successfully created.")
        return redirect('upload_txt')

    return render(request, 'lecturer/upload_txt.html')

@login_required
def select_classes(request):
    profile = LecturerProfile.objects.get(user=request.user)

    if request.method == 'POST':
        form = LecturerClassForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Classes updated.")
            return redirect('lecturer_dashboard')
    else:
        form = LecturerClassForm(instance=profile)

    return render(request, 'lecturer/select_classes.html', {'form': form})

@login_required
def upload_material(request):
    if request.method == 'POST':
        form - ClassMaterialForm(request.POST, request.FILES)
        if form.is_valid():
            material = form.save(commit=False)
            material.uploaded_by = request.user
            material.save()
            return redirect('material_list')
    
    else:
        form = ClassMaterialForm()
    return render(request, 'lecturer/upload_material.html', {'form': form})

@login_required
def material_list(request):
    materials = ClassMaterial.objects.all().order_by('-uploaded_at')
    return render(request, 'stuednt/material_list.html', {'materials': materials})

@login_required
def view_student(request):
    lecturer_profile = LecturerProfile.objcets.get(user=request.user)
    students = StudentProfile.objects.filter(kumpulan_in=lecturer_profile.assigned_kumpulan.all())
    return render(request, 'lecturer/view_students.html', {'students': students})