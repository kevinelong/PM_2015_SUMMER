from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.animals_list, name='animal_list'),
]