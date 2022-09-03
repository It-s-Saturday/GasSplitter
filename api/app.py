from flask import Flask, send_from_directory
from flask_cors import CORS
from flask_restful import Api, Resource, reqparse

app = Flask(__name__, static_folder="../client", static_url_path="")
CORS(app, origins=["*"])
api = Api(app)


@app.route("/hello")
def hello_world():
    print("called hello world")
    return {"text": "<p>Hello, World!</p>", "status": 200}


if __name__ == "__main__":
    app.run("localhost", port=8080, debug=True)
