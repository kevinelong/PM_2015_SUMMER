from django.test import TestCase

from . import forms
from .models import Musician


class TestPasswordMatchingMethods(TestCase):

    def test_has_capital(self):
        result = forms.has_capital('a')
        self.assertFalse(result)

        result = forms.has_capital('A')
        self.assertTrue(result)

        result = forms.has_capital('@')
        self.assertFalse(result)

        result = forms.has_capital(' ')
        self.assertFalse(result)

    def test_has_special_char(self):
        result = forms.has_special_char('A')
        self.assertFalse(result)

        result = forms.has_special_char('aaaaaa&')
        self.assertTrue(result)


class TestCreateUserForm(TestCase):

    def setUp(self):
        self.data = {
            'username': 'reina',
            'first_name': 'reina',
            'last_name': 'abolofia',
            'email': 'purple4reina@gmail.com',
            'password1': 'asdfasdf',
            'password2': 'asdfasdf',
            'instrument': 'CL',
        }

    def test_creates_instrument_field_at_init(self):
        form = forms.CreateUserForm()
        self.assertIsNotNone(form.fields.get('instrument'))

    def test_musician_created_on_save(self):
        self.assertEqual(Musician.objects.count(), 0)

        form = forms.CreateUserForm(self.data)
        form.save()

        self.assertEqual(Musician.objects.count(), 1)

    def test_passwd_too_short(self):

        form = forms.CreateUserForm(self.data)
        self.assertTrue(form.is_valid())

        data = self.data
        data['password1'] = 'asdf'
        data['password2'] = 'asdf'
        form = forms.CreateUserForm(data)
        self.assertFalse(form.is_valid())

        self.assertEqual(
            form.errors,
            {'password1': ['Must be more than 6 chars']}
        )
