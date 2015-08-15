from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^total_clues/$', views.clues_count, name='clues_count'),
]
