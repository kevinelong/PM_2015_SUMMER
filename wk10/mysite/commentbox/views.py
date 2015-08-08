from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.template.context_processors import csrf

from .models import CommentBox
from .forms import CommentForm

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


def comment_page(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('comment_page'))
    else:
        form = CommentForm()

    context = {
        'comments': CommentBox.objects.all(),
        'form': form,
    }
    context.update(csrf(request))

    return render_to_response(
        'comment_return.html',
        context=context,
    )