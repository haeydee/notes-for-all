from django.db import models
from django.contrib.auth.models import User
    
class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    program = models.CharField(max_length=100, blank=True)
    supervisor_email = models.EmailField(blank=True)
    
    def __str__(self):
        return self.user.get_full_name() or self.user.email

class Milestone(models.Model):
    title = models.CharField(max_length=255)
    is_completed = models.BooleanField(default=False)
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='submilestones', on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.title} ({'Done' if self.is_completed else 'Pending'})"