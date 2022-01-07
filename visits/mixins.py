from django.conf import settings
import requests
import json
import re
from datetime import datetime


def get_lat_long(request):
    '''
    takes the latitude and longditude inputed by javascript and posts it to google maps api
    gets the variable directions in a form of a dictionary
    '''
    lat_a = request.POST.get("lat_a")
    long_a = request.POST.get("long_a")
    lat_b = request.POST.get("lat_b")
    long_b = request.POST.get("long_b")
    # this takes the above as parameters and makes API query in mixins
    directions = Directions(
        lat_a=lat_a,
        long_a=long_a,
        lat_b=lat_b,
        long_b=long_b
        )
    # change dictionary to python object ???

    print(f' DIRECTIONS DISTANCE Inside get_lat_long function {directions["distance"]}')
    context = {
        "google_api_key": settings.GOOGLE_API_KEY,
        "lat_a": lat_a,
        "long_a": long_a,
        "lat_b": lat_b,
        "long_b": long_b,
        "origin": f'{lat_a}, {long_a}',
        "destination": f'{lat_b}, {long_b}',
        "directions": directions,
    }

    return context


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
    print(long_b)

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

        # change km to miles and round up to 2 decimal places
        distance = route["distance"]["value"]*0.000621371
        distance = round(distance, 1)
        print(f' ROUND UP {distance}')
        # duration is displayed as a string, not number
        duration = route["duration"]["text"]

    return {
    "origin": origin,
    "destination": destination,
    "distance": distance,
    "duration": duration,
    }


def extract_postcode(full_address):
    '''
    takes a string containing full adress and postcodes and returns postcode only
    Regex from:
    https://stackoverflow.com/questions/164979/regex-for-matching-uk-postcodes
    '''
    matches = re.findall(r'([Gg][Ii][Rr] 0[Aa]{2})|((([A-Za-z][0-9]{1,2})|(([A-Za-z][A-Ha-hJ-Yj-y][0-9]{1,2})|(([A-Za-z][0-9][A-Za-z])|([A-Za-z][A-Ha-hJ-Yj-y][0-9][A-Za-z]?))))\s?[0-9][A-Za-z]{2})', full_address)
    list_of_matches = matches[0]
    postcode = list_of_matches[1]
    return postcode

