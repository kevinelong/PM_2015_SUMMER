from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^comment_page/$', views.comment_page, name='comment_page'),
]