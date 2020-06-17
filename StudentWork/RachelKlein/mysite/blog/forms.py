from django.forms import ModelForm, HiddenInput

from .models import BlogComment


class CommentForm(ModelForm):
    class Meta:
        model = BlogComment
        fields = ('author', 'content', 'article')

    def __init__(self, *args, **kwargs):
        blog_id = kwargs.pop('blog_id')
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['article'].initial = blog_id
        self.fields['article'].widget = HiddenInput()