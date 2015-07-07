__author__ = 'lenny'
"""
I made this file so I can sample one piece of code at a time
Jesse Fitzjarrell
6-29-15
"""

#import statements
from googlemaps import GoogleMaps

#create Googlemaps object
mapservice = GoogleMaps()

#get directions from google
directions = mapservice.directions("Portland", "Bend")

#print each step in directions to console
for step in directions['directions']["routes"][0]['steps']:
    print step['descriptionHtml']