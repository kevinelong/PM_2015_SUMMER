from django import forms
from django.contrib.auth.models import User


class NewUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super(NewUserForm, self).__init__(*args, **kwargs)

        # change help_text for username
        self.fields['username'].help_text = (
            '<br>A string of letters and numbers, must be '
            'between 6 and 12 characters long.'
        )

        # add two password fields
        self.fields['passwd1'] = forms.CharField(
            widget=forms.PasswordInput(),
            required=True,
            label='Password',
        )
        self.fields['passwd2'] = forms.CharField(
            widget=forms.PasswordInput(),
            required=True,
            label='Reenter password',
        )

        # require all fields
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['email'].required = True

    def clean_username(self):
        username = self.cleaned_data['username']
        if len(username) < 6 or len(username) > 12:
            raise forms.ValidationError(
                'Username must be between 6 and 12 characters long')
        elif not username.isalnum():
            raise forms.ValidationError('Username must be letters and numbers only.')
        return username

    def clean_passwd2(self):
        passwd1 = self.cleaned_data['passwd1']
        passwd2 = self.cleaned_data['passwd2']
        if passwd1 != passwd2:
            raise forms.ValidationError(
                'Passwords do not match.'
            )
        return passwd2

    def save(self):
        password = self.cleaned_data['passwd1']
        user = super(NewUserForm, self).save()

        # set the user password
        user.set_password(password)
        user.save()