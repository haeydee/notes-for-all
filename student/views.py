from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Milestone, StudentProfile
from .forms import MajorMilestoneForm, SubMilestoneForm


def dashboard(request):
    if request.user.is_authenticated:
        profile, created = StudentProfile.objects.get_or_create(user=request.user)
        return render(request, 'student_dashboard.html')
    else:
        return redirect('login')

def milestone_view(request):
    profile, created = StudentProfile.objects.get_or_create(user=request.user)
    student = request.user
    major_form = MajorMilestoneForm()
    sub_form = SubMilestoneForm()
    milestones = Milestone.objects.filter(student=profile, parent__isnull=True)
    Milestone.objects.create(student=profile, title="Chapter 1")
    
    if request.method == 'POST':
        if 'add_major' in request.POST:
            major_form = MajorMilestoneForm(request.POST)
            if major_form.is_valid():
                milestone = major_form.save(commit=False)
                milestone.student = student
                milestone.save()
                return redirect('milestone')
        elif 'add_sub' in request.POST:
            sub_form = SubMilestoneForm(request.POST)
            if sub_form.is_valid():
                milestone = sub_form.save(commit=False)
                milestone.student = student
                milestone.save()
                return redirect('milestone')

    return render(request, 'milestone.html', {
        'milestones': milestones,
        'major_form': major_form,
        'sub_form': sub_form,
        'profile': profile
    })

def delete_milestone(request, pk):
    milestone = get_object_or_404(Milestone, pk=pk)

    # Ensure student can only delete their own milestones
    if milestone.student.email == request.user.email:
        milestone.delete()

    return redirect('milestone')

