from app.extensions import db
from app.models.user import User
from flask import Blueprint, abort, jsonify, request
from werkzeug.security import generate_password_hash

users_bp = Blueprint("users", __name__)


@users_bp.route("/users", methods=["POST"])
def create_user():
    """
    Create a new user in the "users" table. The request body should be in JSON format and should contain the following fields:
    {
        "name": "string",
        "email": "string",
        "password": "string"
    }
    
    Route:
        http://localhost:5000/users

    Returns:
        JSON: A JSON object containing the user's name, email, and id (but not the password)
    """
    data = request.get_json()
    new_user = User(
        name=data["name"],
        email=data["email"],
        password=generate_password_hash(
            data["password"], method="pbkdf2:sha256:100", salt_length=8
        ),
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user.to_dict()), 201


@users_bp.route("/users/<uuid:user_id>", methods=["DELETE"])
def delete_user(user_id):
    """
    Delete a user from the "users" table

    Route:
        http://localhost:5000/users/<user_id>

    Params:
        user_id (UUID): The unique identifier of the user

    Returns:
        str: An empty string
    """
    user = User.query.get(user_id)
    if user is None:
        abort(404)
    db.session.delete(user)
    db.session.commit()
    return "", 204
