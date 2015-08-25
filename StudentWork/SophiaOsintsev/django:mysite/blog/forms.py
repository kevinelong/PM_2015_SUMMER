from django.forms import ModelForm

from .models import CommentBox


class CommentsForm(ModelForm):
    class Meta:
        model = PostComment
        fields = ('comment_text', 'user', 'blog_post')