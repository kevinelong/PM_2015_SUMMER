from django import forms
from django.contrib.auth.models import User


class NewUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super(NewUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = (
            '<br>A string of letters and numbers, must be '
            'between 6 and 12 characters long.'
        )
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['email'].required = True

    def clean_username(self):
        username = self.cleaned_data['username']
        if len(username) < 6 or len(username) > 12:
            raise forms.ValidationError(
                'Username must be between 6 and 12 characters long')
        elif not username.isalnum():
            raise forms.ValidationError('Username must be letters and numbers only')
        return username