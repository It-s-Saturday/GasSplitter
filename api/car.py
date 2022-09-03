import requests
import json
from car_secret import CAR_API_KEY
def get_cars(make, model, year, limit, apikey=CAR_API_KEY):
    api_url = 'https://api.api-ninjas.com/v1/cars?model={}&year={}&make={}&limit={}'.format(model, year, make, limit)
    response = requests.get(api_url, headers={'X-Api-Key': apikey})
    if response.status_code == requests.codes.ok:
        car_data = json.loads(response.text)
        return(car_data[0]['combination_mpg'])
    else:
        return("Error:", response.status_code, response.text)
if __name__ == '__main__':
    make = 'toyota'
    model = 'camry'
    year = '1993'
    limit = '1'
    print(get_cars(make, model, year, limit))
