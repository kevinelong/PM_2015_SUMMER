from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^(?P<list_id>\d+)/add_email/$', views.add_email, name='add_email'),
    url(r'^(?P<list_id>\d+)/thanks/$', views.thanks, name='thanks'),
    url(r'^add_to_many/$', views.add_email_to_many, name='add_to_many'),
    url(r'^thanks/$', views.thanks, name='thanks'),
]