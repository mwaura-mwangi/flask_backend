from flask import Flask
from config import DevConfiq
from flask_restx import Api, Resource


app = Flask(__name__)
api = Api(app, doc="/docs", prefix="/api")

app.config.from_object(DevConfiq)

@app.route("/")
def home():
    return "Hello world"

if __name__ == "__main__":
    app.run(debug=True)