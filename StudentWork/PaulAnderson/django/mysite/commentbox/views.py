from django.http import HttpResponse
from django.shortcuts import render_to_response

from .models import CommentBox


def index(request):
    total_comments = CommentBox.objects.count()

    approved_comments = 0
    texts = ''
    for comment in CommentBox.objects.all():
        if comment.approved:
            approved_comments += 1
            texts += comment.comment_text

    return HttpResponse(
        'There are currently {} comment(s).  Their text is: {} {}'.format(total_comments, texts, approved_comments)
    )

def comment_page(request):

    return render_to_response(
        'comment_page.html',
        context={
            'my_comments': CommentBox.objects.all(),
        }
    )
