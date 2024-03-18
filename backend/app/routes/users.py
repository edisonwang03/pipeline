from app.extensions import db
from app.models.users import User
from app.controllers.users import user_exists, create_user, delete_user
from flask import Blueprint, abort, jsonify, request

users_bp = Blueprint("users", __name__)


@users_bp.route("/users", methods=["POST"])
def create_user_route():
    """
    Create a new user in the "users" table. The request body should be in JSON format and should contain the following fields:
    {
        "email": "string",
        "password": "string",
        "name": "string",
    }
    
    Route:
        http://localhost:5000/users

    Returns:
        JSON: A JSON object containing the user's email and name
    """
    data = request.get_json()
    email = data["email"]
    password = data["password"]
    name = data["name"]
    if user_exists(email):
        abort(400)
    new_user = create_user(email, password, name)
    return jsonify(new_user.to_dict()), 201


@users_bp.route("/users/<b32:email>", methods=["DELETE"])
def delete_user_route(email: str):
    """
    Delete a user from the "users" table

    Route:
        http://localhost:5000/users/<b32:email>

    Args:
        email (str): The email of the user to delete. It is initially encoded using the Base32 encoding scheme

    Returns:
        str: An empty string
    """
    if not user_exists(email):
        abort(404)
    delete_user(email)
    return "", 204
