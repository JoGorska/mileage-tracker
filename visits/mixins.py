from django.conf import settings
import requests
import json
import re
from datetime import datetime





def Directions(*args, **kwargs):
    """
    Posts coordinates to google API and gets json response - directions
    created by following tutorial:
    https://www.youtube.com/watch?v=wCn8WND-JpU&t=8s
    """
    lat_a = kwargs.get("lat_a")
    long_a = kwargs.get("long_a")
    lat_b = kwargs.get("lat_b")
    long_b = kwargs.get("long_b")

    origin = f'{lat_a},{long_a}'
    destination = f'{lat_b},{long_b}'

    result = requests.get(
                        'https://maps.googleapis.com/maps/api/directions/json?',
                        params={
                         'origin': origin,
                         'destination': destination,
                         "key": settings.GOOGLE_API_KEY
                        })

    directions = result.json()

    if directions["status"] == "OK":

        route = directions["routes"][0]["legs"][0]
        # this is a string with full address, postcode can be extracted
        origin = route["start_address"]
        destination = route["end_address"]

        # distance in km converted to miles:
        distance = route["distance"]["value"]*0.000621371
        # duration is displayed as a string, not number
        duration = route["duration"]["text"]

    #     steps = [
		# 	[
		# 		s["distance"]["text"],
		# 		s["duration"]["text"],
		# 		s["html_instructions"],

		# 	]
		# 	for s in route["steps"]]

    # return {
		# "origin": origin,
		# "destination": destination,
		# "distance": distance,
		# "duration": duration,
		# "steps": steps
		# }



def extract_postcode(full_address):
    '''
    takes a string containing full adress and postcodes and returns postcode only
    Regex from:
    https://stackoverflow.com/questions/164979/regex-for-matching-uk-postcodes
    '''
    result = ''.join([c for c in full_address if c.isupper()])
    matches = re.findall(r'([Gg][Ii][Rr] 0[Aa]{2})|((([A-Za-z][0-9]{1,2})|(([A-Za-z][A-Ha-hJ-Yj-y][0-9]{1,2})|(([A-Za-z][0-9][A-Za-z])|([A-Za-z][A-Ha-hJ-Yj-y][0-9][A-Za-z]?))))\s?[0-9][A-Za-z]{2})', full_address)
    list_of_matches = matches[0]
    postcode = list_of_matches[1]
    return postcode

