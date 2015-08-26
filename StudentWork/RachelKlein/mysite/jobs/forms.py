from django.forms import ModelForm
from .models import JobPosting
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class JobPostingForm(ModelForm):
    class Meta:
        model = JobPosting
        fields = ('title', 'posting')

class JobRemovalForm(forms.Form):
    selected_job = forms.ChoiceField()

    def __init__(self, *args, **kwargs):
        super(JobRemovalForm, self).__init__(*args, **kwargs)
        choices = [
            (job.id, job.title) for job in JobPosting.objects.all()
        ]

        self.fields['selected_job'].choices = choices

    def save(self):
        job_id = self.cleaned_data['selected_job']
        job_to_delete = JobPosting.objects.get(id=job_id)
        job_to_delete.delete()


class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")