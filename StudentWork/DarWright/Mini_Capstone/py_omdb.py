__author__ = 'darwright'
import requests

from Mini_Capstone import py_omdb_resultlist


class Search(object):

    def __init__(self):
        """
        Sets the default search parameters
        """
        self.imdb_id = '?i='  # A valid IMDb ID (e.g. tt1285016)
        self.title = '?t='  # Movie title to search for.
        self.season = '&Season='  # numeric season number
        self.epi = '&Episode='  # number episode number
        self.s_type = '&type=movie'  # movie, series, episode	Type of result to return.
        self.year = '&y='  # Year of release.
        self.response_type = '&r=json'
        self.plot = '&plot=short'
        self.tomatoes = '&tomatoes=true'
        self.url = 'http://www.omdbapi.com/'
        self.response_list = py_omdb_resultlist.common_list

        # http://www.omdbapi.com/?t=Mad+Max+Fury+Road&y=2015&plot=short&r=json

    def movie(self, title):
        """
        search by title
        """
        self.title = self.title + title
        self.build_url()

    def imdbid(self, imdbid):
        """
        search by imdb ID directly
        """
        self.imdb_id = self.imdb_id + imdbid
        self.build_url()

    def episode(self,in_title, in_season, in_episode):
        """
        alter search defaults for episodes
        example: http://www.omdbapi.com/?t=Game+of+Thrones&Season=3&Episode=1
        """
        self.season = self.season + in_season
        self.epi = self.epi + in_episode
        self.title = self.title + in_title + self.season + self.epi
        self.build_url()

    # Series cane be done via title, does not need to be separated anymore
    # def series(self, title):
    #     """
    #     alter search default for series
    #     This is a basic overview of a series
    #     example: http://www.omdbapi.com/?t=Game+of+Thrones
    #     """
    #     pass

    def build_url(self):
        """
        take the different variables and build the GET url
        """
        # build_url = url + title + year_of_release + plot + response_type
        if self.imdb_id == '?i=':  # blank imdb ID, therefore a movie title search
            self.url = self.url + self.title + self.year + self.plot + self.tomatoes
        else:
            self.url = self.url + self.imdb_id + self.tomatoes

        self.post_url(self.url)
        # TODO error handling

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

    def post_url(self, url):
        """
        GET the info from the url
        """
        response = requests.get(self.url)
        self.parse_response(response)
        pass

    def parse_response(self, response):
        """
        get json response and turn it into a dictionary
        """
        data = response.json()
        self.show_results(data)

    def show_results(self, data):
        """
        print out results based on set response details
        """
        for each in self.response_list:
            value = data[each]
            print "{}: {}".format(each, value)

#
search = Search()
# #
search.episode('Game+of+Thrones', '2', '1')
print search.url

#
# search.imdbid('tt2178782')
# print search.url
#
# print search.imdb_id
# # search.build_url()
# print search.url
