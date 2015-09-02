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

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^recipes/', include([
        url(r'^delete/$', recipes_views.delete_recipe, name='delete_recipe'),
        url(r'^delete-successful/$', recipes_views.delete_successful, name='delete_successful'),
        url(r'^add/$', recipes_views.add_recipe, name='add_recipe'),
        url(r'^all-recipes/$', recipes_views.all_recipes, name='all_recipes'),
        url(r'^(?P<recipe_id>[0-9]+)/$', recipes_views.full_recipe, name='full_recipe'),
    ])),
]
