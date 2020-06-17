from django.forms import ModelForm
from .models import JobPosting, Goal
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
        fields = (
            'username',
            'email',
            'password1',
            'password2')

    def __init__(self, *args, **kwargs):
        super(NewUserForm, self).__init__(*args, **kwargs)
        self.fields['goal_type'] = forms.ChoiceField(
            choices = Goal.GOAL_CATEGORIES,
        )

    def save(self):
        new_user = super(NewUserForm, self).save()
        goal_type = self.cleaned_data['goal_type']
        Goal.objects.create(
            user = new_user,
            goal_type = goal_type,
        )
        password = self.cleaned_data['password1']
        new_user.set_password(password)
        new_user.save()
        return new_user
