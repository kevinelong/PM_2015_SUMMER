from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^(?P<list_id>\d+)/add_email/$', views.add_email, name='add_email'),
    url(r'^(?P<list_id>\d+)/thanks/$', views.thanks, name='thanks'),
]