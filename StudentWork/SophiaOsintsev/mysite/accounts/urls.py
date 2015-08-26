from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^add/$', views.add_user, name='add_user'),
    url(r'^template_fun/$', views.template_fun, name='template-fun'),
]
