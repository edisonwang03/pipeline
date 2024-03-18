from flask_login import login_user, logout_user, login_required, current_user
from app.controllers.users import user_exists, get_user
from werkzeug.security import check_password_hash
from flask import Blueprint, abort, request, jsonify

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["POST"])
def login_route():
    """
    Log in a user by adding their ID to the session. The request body should be in JSON format and should contain the following fields:
    {
        "email": "string",
        "password": "string"
    }

    Route:
        http://localhost:5000/login/<uuid:user_id>

    Returns:
        str: A message indicating that the user has been logged in
    """
    data = request.get_json()
    email = data["email"]
    password = data["password"]
    if not user_exists(email):
        abort(401)
    user = get_user(email)
    if check_password_hash(user.password, password):
        abort(401)
    login_user(user)
    return f"{user} logged in successfully", 200

@auth_bp.route("/logout", methods=["POST"])
@login_required
def logout_route():
    """
    Log out a user by removing their ID from the session

    Route:
        http://localhost:5000/logout

    Returns:
        str: A message indicating that the user has been logged out
    """
    user = current_user
    logout_user()
    return f"{user} logged out successfully", 200




