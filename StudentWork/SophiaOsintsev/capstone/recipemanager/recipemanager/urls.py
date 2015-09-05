"""recipemanager URL Configuration

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

from recipes import views as recipes_views
from accounts import views as accounts_views

urlpatterns = [
    url(r'^reset/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        accounts_views.reset_confirm, name='reset_confirm'),
    url(r'^reset/$', accounts_views.reset, name='reset'),
    url(r'^reset-complete/$', accounts_views.reset_complete, name='reset_complete'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^logout/$', accounts_views.user_logout, name='logout'),
    url(r'^login/$', accounts_views.user_login, name='login'),
    url(r'^register/$', accounts_views.register, name='register'),
    url(r'^recipes/', include([
        url(r'^$', recipes_views.homepage, name='homepage'),
        url(r'^(?P<recipe_id>[0-9]+)/delete/$', recipes_views.delete_recipe, name='delete_recipe'),
        url(r'^delete-successful/$', recipes_views.delete_successful, name='delete_successful'),
        url(r'^add/$', recipes_views.add_recipe, name='add_recipe'),
        url(r'^edit/(?P<recipe_id>[0-9]+)/$', recipes_views.edit_recipe, name='edit_recipe'),
        url(r'^all-recipes/$', recipes_views.all_recipes, name='all_recipes'),
        url(r'^(?P<recipe_id>[0-9]+)/$', recipes_views.full_recipe, name='full_recipe'),
    ])),
]
