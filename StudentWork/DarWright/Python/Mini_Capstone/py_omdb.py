__author__ = 'darwright'
import requests
from Mini_Capstone import py_omdb_resultlist

class Search(object):

    def __init__(self):
        """
        Sets the default search parameters
        """
        self.imdb_id = '?i='  # A valid IMDb ID (e.g. tt1285016)
        self.m_title = u'?t='  # Movie title to search for.
        self.season = '&Season='  # numeric season number
        self.epi = '&Episode='  # number episode number
        self.s_type = '&type=movie'  # movie, series, episode	Type of result to return.
        self.year = '&y='  # Year of release.
        self.response_type = '&r=json'
        self.plot = '&plot=short'
        self.tomatoes = '&tomatoes=true'
        self.url = 'http://www.omdbapi.com/'
        self.response_list = py_omdb_resultlist.common_list
        self.data = {}

    def set_response_details(self, choice):
        """
        set defaults for what info to return/display. ie. long plot, short plot, actors, rotten tomatoes scores etc.
        Some sort of User interaction would take place or be set here
        1 = full list with tomatoes
        2 = full list without tomatoes
        3 = common list ( title, actors, plot, year)
        4 = common list with tomatoes
        """

        if choice == 1:
            self.response_list = py_omdb_resultlist.full_list
        elif choice == 2:
            self.response_list = py_omdb_resultlist.full_list_without_tomatoes
        elif choice == 3:
            self.response_list = py_omdb_resultlist.common_list
        elif choice == 4:
            self.response_list = py_omdb_resultlist.common_list_with_tomatoes

    def title(self, title):
        """
        search by title
        """
        self.m_title = ''
        self.m_title = u'?t=' + title
        self.build_url()

    def imdbid(self, imdbid):
        """
        search by imdb ID directly
        """
        self.imdb_id = self.imdb_id + imdbid
        self.build_url()

    def episode(self, ui_title, ui_season, ui_episode):
        """
        alter search defaults for episodes
        example: http://www.omdbapi.com/?t=Game+of+Thrones&Season=3&Episode=1
        """
        self.season = self.season + ui_season
        self.epi = self.epi + ui_episode
        self.m_title = self.m_title + ui_title + self.season + self.epi
        self.build_url()

    def build_url(self):
        """
        take the different variables and build the GET url
        """
        if self.imdb_id == '?i=':  # blank imdb ID, therefore a movie/series title search
            self.url = self.url + self.m_title + self.year + self.plot + self.tomatoes
        else:
            self.url = self.url + self.imdb_id + self.tomatoes

        self.post_url()

    def post_url(self):
        """
        GET the info from the url
        """
        response = requests.get(self.url)
        if response == '<Response [200]>':
            raise TimeoutError('Web service timed out')
        else:
            self.parse_response(response)

    def parse_response(self, response):
        """
        get json response and turn it into a dictionary
        """
        self.data = response.json()


class TimeoutError(Exception):
    """
    When the request module gets back a response 200, give  time out error
    """
