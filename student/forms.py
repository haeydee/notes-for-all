from django import forms
from .models import Milestone

class MajorMilestoneForm(forms.ModelForm):
    class Meta:
        model = Milestone
        fields = ['title']
    
class SubMilestoneForm(forms.ModelForm):
    class Meta:
        model = Milestone
        fields = ['title', 'parent']