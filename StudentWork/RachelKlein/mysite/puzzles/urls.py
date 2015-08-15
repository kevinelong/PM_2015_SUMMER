from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^welcome/$', views.welcome, name='welcome'),
    url(r'^total_clues/$', views.clues_count, name='clues_count'),
    url(r'^small_width/$', views.small_width, name='small_width'),
    url(r'^devilish/$', views.devilish, name='devilish'),
    url(r'^easy_n/$', views.easy_n, name='easy_n'),
    url(r'not_ten/$', views.not_ten, name='not_ten'),
    url(r'puzzles_by_clue/$', views.puzzles_by_clue, name='puzzles_by_clue'),
]
