from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^availability/$', views.availability, name='availability'),
]