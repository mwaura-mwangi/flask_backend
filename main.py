from flask import Flask
from config import DevConfig
from database.exts import db
from api.user_routes import user_ns
from flask_restx import Api, Resource

# Initialize the Flask application instance
app = Flask(__name__)

# Initialize Flask-RESTX API extension
# - doc="/docs": Sets the Swagger UI documentation route to http://127.0.0.1:5000/docs
# - prefix="/api": Prefixes all API routes with /api (e.g., /api/users/)
api = Api(app, doc="/docs", prefix="/api")

# Load development configuration settings (database URIs, secret keys, etc.) from DevConfig
app.config.from_object(DevConfig) # load devconfig settings

# Register the users namespace (imported from api.user_routes) into the API
api.add_namespace(user_ns)

# (Note: This duplicate config loading line re-applies DevConfig, though it's redundant since it was already loaded above)
app.config.from_object(DevConfig)


# Initialise the SQLAlchemy database extension with the Flask app instance
db.init_app(app)

# Define a root route for testing if the web server is running
@app.route("/")
def home():
    return "Hello world"
    
# Run the Flask development server if this script is executed directly
if __name__ == "__main__":
    app.run(debug=True)