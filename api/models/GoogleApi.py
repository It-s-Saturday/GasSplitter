import os

import googlemaps
import requests

cwd = os.getcwd()
print(cwd)

if os.path.exists(f"{cwd}/models/secrets.py"):
    from .secrets import GOOGLE_API_KEY
else:
    raise Exception("No secrets.py found!")


class GoogleApi:
    def __init__(self):
        self.api_key = GOOGLE_API_KEY
        self.gmaps = googlemaps.Client(key=self.api_key)

    def lookup(self, origin_in, destination_in):
        """Uses the GoogleMaps API to retrieve a JSON that contains the duration and distance between the origin_in and
        destination_in)"""
        origin = origin_in.replace(" ", "+")
        destination = destination_in.replace(" ", "+")
        print("G", origin, destination)
        url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&"
        concat = f"{url}origins={origin}&destinations={destination}&key={self.api_key}&mode=driving"
        print(concat)
        r = requests.get(concat)
        measurement = r.json()["rows"][0]["elements"][0]["distance"]["text"]
        print(measurement)
        return measurement
