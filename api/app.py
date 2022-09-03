import googlemaps
import car
from flask import Flask, send_from_directory
from flask_cors import CORS
from flask_restful import Api, Resource, reqparse
from twilio_util import Twilio
from gas import get_gas
from models import GoogleApi

app = Flask(__name__, static_folder="../client", static_url_path="")
CORS(app, origins=["*"])
api = Api(app)

app.rider_count = 0
app.mpg = 0
app.distance = 0


@app.route("/hello")
def hello_world():
    print("called hello world")
    return {"text": "<p>Hello, World!</p>", "status": 200}


@app.route("/get_mpg/<make>/<model>/<year>")
def getMPG(make, model, year):
    # add mostafa implementation
    app.mpg = car.get_cars(make, model, year)
    print(app.mpg)
    return {"text": "Success", "value": int(app.mpg), "status": 200}


# post
@app.route("/set_rider_count/<count>")
def setRiderCount(count):
    status = 200
    try:
        app.rider_count = count
        print(app.rider_count)
    except:
        status = 400
    return {"status": status}


@app.route("/distance/<origin>/<destination>")
def distance(origin, destination):
    # implement google call here
    print(origin, destination)
    try:
        google_driver = GoogleApi.GoogleApi()
        app.distance = google_driver.lookup(origin, destination)
        return {"distance": app.distance, "status": 200}
    except:
        return {"status": 400}


@app.route("/calculate/<make>/<model>/<year>/<origin>/<destination>/<count>")
def calculate(make, model, year, origin, destination, count):
    mpg = car.get_cars(make, model, year)
    google_driver = GoogleApi.GoogleApi()
    distance = google_driver.lookup(origin, destination)[:-3].replace(",", "")
    multiply = int(distance) / int(mpg)
    price = get_gas()
    divide = round(float(price) * int(multiply), 2)
    return {"text": f"Each person owes {divide}", "value": divide, "status": 200}

@app.route("/send/<numbers>/<message>")
def send(numbers, message):
    twilio = Twilio()
    twilio.message_user_list([numbers], message)
    return {"status": 200}

@app.route("/test")
def test():
    r1 = requests.get("http://localhost:8080/get_mpg/test_make/test_model")
    r2 = requests.get("http://localhost:8080/")


if __name__ == "__main__":
    app.run("localhost", port=8080, debug=True)
