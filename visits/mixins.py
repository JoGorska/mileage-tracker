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

        # change km to miles and round up to 1 decimal place
        distance = route["distance"]["value"]*0.000621371
        distance = round(distance, 1)
        # duration is displayed as a string, not number
        duration = route["duration"]["text"]

    return {
        "origin": origin,
        "destination": destination,
        "distance": distance,
        "duration": duration,
        }


def extract_postcode(googe_places_full_addr, google_directions_full_addr):
    '''
    takes a string containing full adress and postcodes and returns postcode 
    only checks if postscode can be found in one of the possible matches,
    if no postcode found it returns google_places full address
    Regex from:
    https://stackoverflow.com/questions/164979/regex-for-matching-uk-postcodes
    '''
    regex = (r'([Gg][Ii][Rr] 0[Aa]{2})|((([A-Za-z][0-9]{1,2})|(([A-Za-z][A-Ha-'
             r'hJ-Yj-y][0-9]{1,2})|(([A-Za-z][0-9][A-Za-z])|([A-Za-z][A-Ha-hJ-'
             r'Yj-y][0-9][A-Za-z]?))))\s?[0-9][A-Za-z]{2})')

    matches_places = re.findall(regex, googe_places_full_addr)
    matches_directions = re.findall(regex, google_directions_full_addr)

    if len(matches_directions) == 0 and len(matches_places) == 0:
        postcode = googe_places_full_addr

    elif len(matches_places) == 0:
        list_of_matches_directions = matches_directions[0]
        postcode = list_of_matches_directions[1]

    else:
        list_of_matches_places = matches_places[0]
        postcode = list_of_matches_places[1]


    return postcode
