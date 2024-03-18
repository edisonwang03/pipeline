import uuid
from backend.app.models.users import User, load_user
from flask_login import login_user, logout_user, login_required
from werkzeug.security import check_password_hash
from flask import Blueprint, abort, request

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login/<uuid:user_id>", methods=["POST"])
def login(user_id):
    """
    Log in a user by adding their ID to the session

    Route:
        http://localhost:5000/login/<uuid:user_id>

    Returns:
        str: A message indicating that the user has been logged in
    """
    user = load_user(user_id)
    if user is None or not check_password_hash(user.password, request.json["password"]):
        abort(401)
    login_user(user)
    return "Logged in successfully", 200

@auth_bp.route("/logout", methods=["POST"])
@login_required
def logout():
    """
    Log out a user by removing their ID from the session

    Route:
        http://localhost:5000/logout

    Returns:
        str: A message indicating that the user has been logged out
    """
    logout_user()
    return "Logged out successfully", 200




