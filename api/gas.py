from asyncio.windows_events import NULL
from genericpath import isfile
import json
import requests
import os

cwd = os.getcwd()
print(isfile(f'{cwd}/api/mock_gas_price.json'))

if  isfile(f'{cwd}/api/mock_gas_price.json'):
    with open(f'{cwd}/api/mock_gas_price.json') as f:
        mock_gas_price = json.load(f)
        print(mock_gas_price['result']['state']['gasoline'])
else:
    url = "https://gas-price.p.rapidapi.com/stateUsaPrice"

    querystring = {"state":"WA"}

    headers = {
        "X-RapidAPI-Key": "7ecb8b990fmsh4dd92222a29eb72p1de777jsn388d89d19302",
        "X-RapidAPI-Host": "gas-price.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)