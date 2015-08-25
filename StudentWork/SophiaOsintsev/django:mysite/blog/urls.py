from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^page-with-links/$', views.page_with_links, name='page_with_links'),
    url(r'^all-entries/$', views.all_entries, name='all_entries'),
    url(r'^article/([0-9]+)/$', views.blog_article, name='blog_article'),
    url(r'^about/$', views.about_page, name='about_page'),

]

