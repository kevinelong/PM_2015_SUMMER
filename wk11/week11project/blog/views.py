from django.shortcuts import render_to_response

from .models import BlogArticle


def page_with_links(request, id=None):
    return render_to_response(
        'blog_list.html',
        context={
            'blogs': BlogArticle.objects.all(),
        }
    )


def blog_article(request, blog_id):
    blog = BlogArticle.objects.get(id=blog_id)
    return render_to_response(
        'blog_detail.html',
        context={
            'blog': blog,
        }
    )