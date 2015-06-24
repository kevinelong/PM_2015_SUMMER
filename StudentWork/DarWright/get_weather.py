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
        locations = pywapi.get_loc_id_from_weather_com(location) # this returns a dictionary looking item
        # This is ugly, is there a better way?
        location_list = locations[0]  # get the first item out of the dict, the key is 0 - this returns a tuple!
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
        if len(location_id) == 5:
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
# print weather.get_weather(city_id)
# print weather.get_weather('87123')


