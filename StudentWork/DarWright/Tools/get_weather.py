import pywapi
import string

class Weather(object):
    def __init__(self):
        self.given_location = ''

    def get_id_by_location(self, location):
        """
        enter a city name and retrieve the top ID result from weather.com
        can enter just a city name (Portland),
        or a city name and State code code example:( Portland, OR)
        or a city name and full state name example: (Portland, Oregon)
        """
        self.given_location = location
        locations = pywapi.get_loc_id_from_weather_com(location) # this returns a dictionary
        # returns: {0: (u'USOR0275', u'Portland, OR'), 'count': 1}
        # returns {'count': 0}
        for x in locations:
            if locations['count'] == '0':
                location_id = '0000'
                return location_id
        else:
            location_list = locations[0]  # get the first item out of the dict, the key is 0 - this returns a tuple
            location_list = str(location_list)  # change it to a string
            location_list = location_list.split()  # split the string into a list
            location_id = location_list[0]  # pull first element out of the list
            location_id = location_id[3:-2]  # strip the u'\ off the front and ', ' off the end.
            return location_id

    def get_weather(self, location_id):
        """
        can enter location ID from weather.com
        or 5 digit zip code
        """
        if len(location_id) < 5:
            results = "No match for location entered could be found."

        elif len(location_id) == 5:
            weather_com_result = pywapi.get_weather_from_weather_com(location_id, units='imperial')
            results = "According to Weather.com: It is " + \
                      string.lower(weather_com_result['current_conditions']['text']) + \
                      " and " + weather_com_result['current_conditions']['temperature'] + \
                      "F now in zip code %s .\n\n" % location_id

        else:
            weather_com_result = pywapi.get_weather_from_weather_com(location_id, units='imperial')
            results = "According Weather.com: It is " + \
                      string.lower(weather_com_result['current_conditions']['text']) + \
                      " and " + weather_com_result['current_conditions']['temperature'] + \
                      "F now in %s.\n\n" % self.given_location
        return results


# weather = Weather()
# city_id = weather.get_id_by_location('Portland, Oregon')
# print city_id
# print weather.get_weather(city_id)
# print weather.get_weather('87123')

# UNIT TESTS

def test_bad_location():
    weather = Weather()
    city_id = weather.get_id_by_location('Pasdkjl')
    print "test returned id: ", city_id
    print weather.get_weather(city_id)
    assert(city_id != 0000)
# test_bad_location()

def test_good_location_city():
    weather = Weather()
    city_id = weather.get_id_by_location('Portland')
    print "test returned id: ", city_id
    assert(city_id != 'USOR0275')
    # not sure why i get an AssertionError here.
# test_good_location_city()

def test_good_location_city_state_code():
    weather = Weather()
    city_id = weather.get_id_by_location('Portland, OR')
    print "test returned id: ", city_id
    assert(city_id != 'USOR0275')
    # not sure why i get an AssertionError here.
# test_good_location_city_state_code()

def test_good_location_city_state_full():
    weather = Weather()
    city_id = weather.get_id_by_location('Portland, Oregon')
    print "test returned id: ", city_id
    assert(city_id != 'USOR0275')
    # not sure why i get an AssertionError here.
# test_good_location_city_state_full()

def test_bad_zip_code():
    weather = Weather()
    city_id = weather.get_id_by_location('00000')
    print "test returned id: ", city_id
    assert(city_id != '0000')
test_bad_zip_code()

def test_good_location_zip():
    weather = Weather()
    city_id = weather.get_id_by_location('97218')
    print "test returned id: ", city_id
    assert(city_id != 'USOR0275')
    # not sure why i get DON'T get AssertionError here.
# test_good_location_zip()

def test_good_location_zip_plus_four():
    weather = Weather()
    city_id = weather.get_id_by_location('97218-1946')
    print "test returned id: ", city_id
    assert(city_id != 'USOR0275')
    # not sure why i get DON'T get AssertionError here.
# test_good_location_zip_plus_four()