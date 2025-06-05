from django import forms
from .models import Milestone, Submission, Comment

class MilestoneForm(forms.ModelForm):
    class Meta:
        model = Milestone
        fields = ['title', 'description', 'due_date']

class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ['title','file']
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 3}),
        }
        