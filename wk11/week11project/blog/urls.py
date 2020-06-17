from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^page-with-links/(?P<blog_id>[0-9]{4})/$', views.page_with_links, name='page_with_links'),
    url(r'^page-with-links/$', views.page_with_links, name='page_with_links'),
]