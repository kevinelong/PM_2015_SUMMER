import urllib2
import json

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
        # Send the url out and get a json response back
        response = urllib2.urlopen(build_url)
        # parse? json is like a dictionary, everything is in unicode.
        data = json.load(response)
        # print data
        if data['Response'] == "False":
            print "No match found for: {}.".format(title_input)
        else:
            print "Title: ", data['Title'], "\nYear: ", data['Year'], "\nPlot: ", data['Plot'], \
                "\nActors: ", data['Actors']


new = MovieSearch()
new.search_by_title('Gravity')
new.search_by_title('I am not a real movie')





