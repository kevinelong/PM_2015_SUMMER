from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<animal_id>[0-9]+)/$', views.animals_list, name='animal_list'),
]