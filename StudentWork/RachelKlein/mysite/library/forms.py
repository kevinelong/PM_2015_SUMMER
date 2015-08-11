from django.forms import ModelForm

from .models import Book


class BookRequestForm(ModelForm):
    class Meta:
        model = Book
        fields = ('name', 'ISBN')
