from flask import Flask, send_from_directory
from flask_cors import CORS
from flask_restful import Api, Resource, reqparse

app = Flask(__name__, static_folder="../client", static_url_path="")
CORS(app, origins=["*"])
api = Api(app)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    app.run("localhost", port=3000, debug=True)