from flask import request
from model.users import User
from utils.custom_decorator import expect
from flask_restx import Resource, Namespace, fields

# Create a Flask-RESTX Namespace for grouping user-related API endpoints under "/users"
user_ns = Namespace("users", description="A namespace for Users")

# Define the API data model for Swagger documentation and serialization/marshalling
user_api_model = user_ns.model(
    "User",
    {
        "id": fields.Integer(),
        "name": fields.String(),
        "email": fields.String(),
        "department": fields.String(),
        "designation": fields.String(),
        "contact": fields.String(),
        "role": fields.String(),
        "manager_id": fields.Integer(),
    },
)

# Route handler for the base collection endpoint: "/users/"
@user_ns.route("/")
class UsersResource(Resource):
    # @expect → Validates the input
    # @marshal_with → Formats the output

    # GET method: Retrieves and returns a list of all users
    @user_ns.marshal_list_with(user_api_model)
    def get(self):
        """Get all users"""
        # Query the database for all user records
        employees = User.query.all()
        # Automatically serialize/format the list of objects using the user_api_model
        return employees

    # POST method: Creates a new user record
    @user_ns.marshal_with(user_api_model)
    # @user_ns.expect(user_api_model)
    @expect(user_ns, user_api_model, ["id"])  # Custom decorator to validate incoming JSON payload against the model
    def post(self):
        """Create a new user"""
        # Extract the JSON body sent with the HTTP request
        data = request.get_json()

        # Instantiate a new User object using data from the request payload
        new_user = User(
            name = data.get("name"),
            email = data.get("email"),
            department = data.get("department"),
            designation = data.get("designation"),
            contact = data.get("contact"),
            role = data.get("role"),
            manager_id = data.get("manager_id"),
        )
        # Save the new user record to the database
        new_user.save()
        # Return the newly created user object (which gets marshalled by @user_ns.marshal_with)
        return new_user

# Route handler for specific user operations by ID: "/users/<id>"
@user_ns.route("/<int:id>")
class UserResource(Resource):

    # GET method: Retrieve a single user's details by their unique ID
    @user_ns.marshal_with(user_api_model)
    def get(self, id):
        """Get a user details by id"""
        # Query the database for the user, or automatically return a 404 Not Found error if the ID doesn't exist
        user = User.query.get_or_404(id)
        return user

    # PUT method: Update an existing user's information by ID
    @expect(user_ns, user_api_model, ["id"])
    def put(self, id):
        """Update a user by id"""
        # Find the employee to update or return 404 if not found
        employee_to_update = User.query.get_or_404(id)
        # Get the updated data from the request body
        data = request.get_json()
        # Call the model's update method with the new field values
        employee_to_update.update(
            data.get("name"),
            data.get("email"),
            data.get("department"),
            data.get("designation"),
            data.get("contact"),
            data.get("role"),
            data.get("manager_id"),
        )
        # Return a success message confirmation dictionary
        return {"message": "User updated successfully."}

    # DELETE method: Remove a user from the database by ID
    def delete(self, id):
        """Delete a user by id"""
        # Find the user to delete or return 404 if not found
        user_to_delete = User.query.get_or_404(id)
        # Call the model's delete method to remove the record
        user_to_delete.delete()
        # Return a success message confirmation dictionary
        return {"message": "User deleted successfully."}