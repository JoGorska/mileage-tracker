from django.conf import settings
import requests
import json
import re


def extract_postcode(full_address):
    result = ''.join([c for c in full_address if c.isupper()])
    matches = re.findall(r'([Gg][Ii][Rr] 0[Aa]{2})|((([A-Za-z][0-9]{1,2})|(([A-Za-z][A-Ha-hJ-Yj-y][0-9]{1,2})|(([A-Za-z][0-9][A-Za-z])|([A-Za-z][A-Ha-hJ-Yj-y][0-9][A-Za-z]?))))\s?[0-9][A-Za-z]{2})', full_address)
    list_matches = matches[0]
    postcode = list_matches[1]
    return postcode


def Directions(*args, **kwargs):
    """
    Handles directions from Google
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
        # this is a string, postcode can be taken out of it counting positions of letters from the end of the string
        # postcodes can be shorter and longer:
        # M3 3EH or SW1A 2AB
        origin = route["start_address"]
        destination = route["end_address"]
        # route is an object consisiting of text and value
        # route["distance"]["text"] - returns 444 km, while route["distance"]["value"] returns 444
        # I recalculate km to miles

        distance = route["distance"]["value"]*0.000621371
        duration = route["duration"]["text"]

        steps = [
			[
				s["distance"]["text"],
				s["duration"]["text"],
				s["html_instructions"],

			]
			for s in route["steps"]]

    return {
		"origin": origin,
		"destination": destination,
		"distance": distance,
		"duration": duration,
		"steps": steps
		}
