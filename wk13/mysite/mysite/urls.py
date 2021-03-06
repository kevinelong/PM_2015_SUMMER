"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from jobposts import views as jobpost_views
from accounts import views as accounts_views


urlpatterns = [
    url('^', include('django.contrib.auth.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', auth_views.login),
    url(r'^jobs/', include([
        url(r'^create/$', jobpost_views.create_post, name='create_jobpost'),
        url(r'^(?P<job_id>[0-9]+)/update/$', jobpost_views.update_post, name='update_jobpost'),
        url(r'^$', jobpost_views.jobs_list, name='jobs_list'),
        url(r'^(?P<job_id>[0-9]+)/$', jobpost_views.job_detail, name='job_detail'),
        url(r'^(?P<job_id>[0-9]+)/delete/$', jobpost_views.delete_post, name='delete_jobpost'),
    ])),
    url(r'^accounts/', include([
        # do not use this! there is a better way! (just this one --v )
        url(r'^(?P<user_id>\d+)/change_password/$', accounts_views.change_password, name='change_password'),
        url(r'^(?P<user_id>\d+)/$', accounts_views.user_detail, name='user_detail'),
        url(r'^create/$', accounts_views.create_user, name='create_user'),
    ])),
]
