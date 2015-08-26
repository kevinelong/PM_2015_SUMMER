from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^page-with-links/$', views.page_with_links, name='page_with_links'),
    url(r'^all-blog-entries/$', views.page_with_links, name='page_with_links'),
    url(r'^(?P<blog_id>[0-9]+)/$', views.individual_entry, name='individual_entry'),
    url(r'^about/$', views.about, name='about_page'),
    url(r'^comments/(?P<blog_id>[0-9]+)/$', views.comment_page, name='comment_page'),
    url(r'^thanks/$', views.about, name='comment_thanks'),
    url(r'^comments/delete_comment/(?P<comment_id>\d+)/$', views.delete_comment, name='delete_comment'),
    url(r'^comments/edit_comment/(?P<comment_id>\d+)/$', views.edit_comment, name='edit_comment'),
]
