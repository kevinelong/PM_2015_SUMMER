from django import forms

from .models import JobPost

class JobCreateForm(forms.ModelForm):
    class Meta:
        model = JobPost
        exclude = []