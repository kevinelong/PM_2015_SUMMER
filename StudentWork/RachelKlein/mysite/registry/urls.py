from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^(?P<wedding_id>\d+)/purchase/$', views.purchase, name='purchase'),
]