from django.forms import ModelForm

from .models import BlogComment


class CommentForm(ModelForm):
    class Meta:
        model = BlogComment
        fields = ('author', 'content', 'article')