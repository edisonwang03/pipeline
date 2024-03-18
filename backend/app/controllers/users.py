from app.extensions import db, login_manager
from app.models.users import User
from werkzeug.security import generate_password_hash


@login_manager.user_loader
def load_user(email: str):
    """
    A callback function that is used to reload the user object from the user email stored in the session.

    Args:
        email (str): The email of the user

    Returns:
        User: The user object
    """
    return User.query.get(email)

def user_exists(email: str) -> bool:
    """
    Check if a user exists in the "users" table

    Args:
        email (str): The email of the user

    Returns:
        bool: True if the user exists, False otherwise
    """
    return User.query.filter_by(email=email).first() is not None

def get_user(email: str) -> User:
    """
    Get a user from the "users" table

    Args:
        email (str): The email of the user

    Returns:
        User: The user
    """
    return User.query.get(email)

def create_user(email: str, password: str, name: str) -> User:
    """
    Create a new user in the "users" table

    Args:
        email (str): The email of the user
        password (str): The password of the user
        name (str): The name of the user

    Returns:
        User: The new user
    """
    new_user = User(
        email=email,
        password=generate_password_hash(
            password, method="pbkdf2:sha256:100", salt_length=8
        ),
        name=name,
    )
    db.session.add(new_user)
    db.session.commit()
    return new_user

def delete_user(email: str) -> None:
    """
    Delete a user from the "users" table

    Args:
        email (str): The email of the user
    """
    user = User.query.get(email)
    db.session.delete(user)
    db.session.commit()