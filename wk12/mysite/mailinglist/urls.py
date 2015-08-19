from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^add_email/$', views.add_email, name='add_email'),
    url(r'^thanks/$', views.thanks, name='thanks'),
]