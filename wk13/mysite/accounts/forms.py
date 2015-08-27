from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Musician


class ChangePasswordForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('password',)

    def __init__(self, *args, **kwargs):
        super(ChangePasswordForm, self).__init__(*args, **kwargs)
        self.fields['password'].widget = forms.PasswordInput()
        self.fields['password2'] = forms.CharField(
            widget=forms.PasswordInput(),
            label='Password Confirm',
        )

    def clean_password(self):
        pw = self.cleaned_data['password']
        if len(pw) < 6:
            raise forms.ValidationError('Password must be at least 6 characters long')
        elif not has_capital(pw):
            raise forms.ValidationError('Password must have capital letter')
        elif not has_lower(pw):
            raise forms.ValidationError('Password must have lower case letter')
        elif not has_number(pw):
            raise forms.ValidationError('Password must have a number')
        elif not has_special_char(pw):
            raise forms.ValidationError(
                'Password must have a special character (but I\'m not gonna tell you what they are)')
        return pw

    def clean_password2(self):
        pw = self.cleaned_data.get('password')
        pw2 = self.cleaned_data['password2']
        if not pw:
            return pw2
        if pw != pw2:
            raise forms.ValidationError('Passwords do not match!')
        return pw2

    def save(self):
        user = super(ChangePasswordForm, self).save()
        new_pw = self.cleaned_data['password']
        user.set_password(new_pw)
        user.save()


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        )

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        self.fields['instrument'] = forms.ChoiceField(
            choices=Musician.INSTRUMENT_CHOICES,
        )

    def save(self):
        new_user = super(CreateUserForm, self).save()

        instrument = self.cleaned_data['instrument']
        Musician.objects.create(
            user=new_user,
            instrument=instrument,
        )

        pw = self.cleaned_data['password1']
        new_user.set_password(pw)
        new_user.save()
        return new_user


def has_capital(word):
    """
    Given a string, returns True if there is a capital letter in it
    """
    for char in word:
        if char.isupper():
            return True
    return False


def has_lower(word):
    """
    docstring goes here!
    :param word:
    :return:
    """
    for char in word:
        if char.islower():
            return True
    return False


def has_special_char(word):
    special_chars = '!@#$%^&*()'
    for special_char in special_chars:
        if special_char in word:
            return True
    return False


def has_number(word):
    for char in word:
        if char.isdigit():
            return True
    return False