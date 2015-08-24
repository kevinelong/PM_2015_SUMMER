from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'posting_site/$', views.posting_site, name='posting_site'),
    url(r'remove_posting/$', views.remove_posting, name='remove_posting'),
]