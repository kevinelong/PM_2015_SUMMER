from django.forms import ModelForm

from .models import CommentBox

class CommentForm(ModelForm):
    class Meta:
        model = CommentBox
        fields = ('comment_text', 'user', 'blog_post')
