from django.http import HttpResponse

from .models import CommentBox


def index(request):
    total_comments = CommentBox.objects.count()

    texts = ''
    for comment in CommentBox.objects.all():
        if comment.approved:
            texts += comment.comment_text

    return HttpResponse(
        'There are currently {} comment(s). Their text is: {}'.format(
            total_comments, texts)
    )