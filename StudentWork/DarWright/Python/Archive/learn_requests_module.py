__author__ = 'darwright'
import requests


class MovieSearch(object):

    def search_by_title(self, title_input, year_input=''):
        url = 'http://www.omdbapi.com/?'
        check_for_space = title_input.replace(' ', '+')
        title = 't=' + check_for_space
        year_of_release = '&y=' + year_input
        plot = '&plot=short'
        response_type = '&r=json'
        # build the URL from all the above pieces
        build_url = url + title + year_of_release + plot + response_type
        # Send the url out and get a response back
        response = requests.get(build_url)
        # put into a dict file using json
        data = response.json()
        if data['Response'] == "False":
            print "No match found for: {}.".format(title_input)
        else:
            print "Title: ", data['Title'], "\nYear: ", data['Year'], "\nPlot: ", data['Plot'], \
                "\nActors: ", data['Actors']


new = MovieSearch()
new.search_by_title('Gravity')
new.search_by_title('I am not a real movie')