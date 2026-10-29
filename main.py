from flask import Flask
from config import DevConfiq
from database.exts import db
from api.user_routes import user_ns
from flask_restx import Api, Resource


app = Flask(__name__)
api = Api(app, doc="/docs", prefix="/api")

api.add_namespace(user_ns)

app.config.from_object(DevConfiq)


# Initialise the database
db.init_app(app)

@app.route("/")
def home():
    return "Hello world"

if __name__ == "__main__":
    app.run(debug=True)