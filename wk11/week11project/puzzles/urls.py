from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.home_page, name='puzzles_home'),
    url(r'^total_clues/$', views.clues_count, name='clues_count'),
    url(r'^clues_width_less_than/(\d+)/$', views.clues_width_less_than, name='clues_width_less_than'),
    url(r'^devilish_clues/$', views.devilish_clues, name='devilish_clues'),
    url(r'^clue/$', views.clues_list, name='clues_list'),
    url(r'^clue/(?P<clue_id>\d+)/$', views.clue_detail, name='clue_detail'),
    url(r'^puzzle/(?P<puzzle_id>\d+)/$', views.puzzle_detail, name='puzzle_detail'),
]
