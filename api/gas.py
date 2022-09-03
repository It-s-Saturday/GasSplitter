from asyncio.windows_events import NULL
from genericpath import isfile
from car_secret import GAS_API_KEY
import json
import requests
import os


def get_gas_price():
    cwd = os.getcwd()
    print(isfile(f"{cwd}/api/mock_gas_price.json"))
    if isfile(f"{cwd}/api/mock_gas_price.json"):
        with open(f"{cwd}/api/mock_gas_price.json") as f:
            mock_gas_price = json.load(f)
            print(mock_gas_price["result"]["state"]["gasoline"])
    else:
        url = "https://gas-price.p.rapidapi.com/stateUsaPrice"

        querystring = {"state": "WA"}

        headers = {
            "X-RapidAPI-Key": GAS_API_KEY,
            "X-RapidAPI-Host": "gas-price.p.rapidapi.com",
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        print(response.text)
