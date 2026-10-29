from flask import request
from model.users import User
from flask_restx import Resource, Namespace, fields

user_ns = Namespace("users", description="A namespace for users")


user_api_model = user_ns.model(
    "User",
    {
        "id": fields.Integer(),
        "name": fields.String(),
        "email": fields.String(),
        "department": fields.String(),
        "contact": fields.String(),
        "role": fields.String(),
        "manager_id": fields.Integer(),
    }
)

@user_ns.route("/")
class UsersResource(Resource):
    def get(self):
        """Get all users"""
        employees = User.query.all()
        return employees

    def post(self):
        """Create a new user"""
        data = request.get_json()
        
        new_user = User(
            name = data.get("name"),
            email = data.get("email"),
            department = data.get("department"),
            designation = data.get("designation"),
            contact = data.get("contact"),
            role = data.get("role"),
            manager_id = data.get("manager_id")
        )

        new_user.save()
        return new_user

    @user_ns.route("/<int:id>")
    class UserResource(Resource):
        def get(self, id):
            """Get a user details by id"""
            user = User.query.get_or_404(id)
            return user

        def put(self, id):
            """update a user by id"""
            user_to_update = User.query.get_or_404(id)
            data = request.get_json()
            user_to_update.update(
                name = data.get("name"),
                email = data.get("email"),
                department = data.get("department"),
                designation = data.get("designation"),
                contact = data.get("contact"),
                role = data.get("role"),
                manager_id = data.get("mananger_id")
            )
            return {"message": "User updated successfully."}


        def delete(self, id):
            """Delete a user by Id"""

            