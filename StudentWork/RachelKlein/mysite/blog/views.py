from django.shortcuts import render_to_response

from .models import BlogArticle
import random
from forms import CommentForm
from django.core.urlresolvers import reverse
from django.template.context_processors import csrf


def page_with_links(request):
    return render_to_response(
        'blog_list.html',
        context={
            'blogs': BlogArticle.objects.all(),
        }
    )

def individual_entry(request, blog_id=None):
    return render_to_response(
        'blog_entry.html',
        context={
            'blog_entry': BlogArticle.objects.get(id=blog_id),
        }
    )

def about(request):
    random_entry_id = random.randrange(1, BlogArticle.objects.count())
    return render_to_response(
        'about.html',
        context={
            'random_entry': BlogArticle.objects.get(id=random_entry_id)
        }
    )

def comment_page(request, blog_id=None):

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('comment_thanks'))
    else:
        form = CommentForm()

    context={
            'form': form.as_p(),
            'blog_entry': BlogArticle.objects.get(id=blog_id)
        }
    context.update(csrf(request))

    return render_to_response(
        'comment_page.html',
        context=context
    )