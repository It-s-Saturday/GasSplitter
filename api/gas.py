from genericpath import isfile
from car_secret import GAS_API_KEY
import json
import requests
import os

cwd = os.getcwd()
print(isfile(f"{cwd}/mock_gas_price.json"))

def get_gas():
    print(cwd)
    if isfile(f"{cwd}/mock_gas_price.json"):
        with open(f"{cwd}/mock_gas_price.json") as f:
            mock_gas_price = json.load(f)
            # print(mock_gas_price["result"]["state"]["gasoline"])
            return mock_gas_price["result"]["state"]["gasoline"]
    else:
        url = "https://gas-price.p.rapidapi.com/stateUsaPrice"

        querystring = {"state": "PA"}

        headers = {
            "X-RapidAPI-Key": GAS_API_KEY,
            "X-RapidAPI-Host": "gas-price.p.rapidapi.com",
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        mock_gas_price = response.text
        return mock_gas_price["result"]["state"]["gasoline"]

if __name__ == "__main__":
    print(get_gas())