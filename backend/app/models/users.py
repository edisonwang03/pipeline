import uuid
from typing import Dict, Union

from app.extensions import db, login_manager
from flask_login import UserMixin
from sqlalchemy.dialects.postgresql import UUID

@login_manager.user_loader
def load_user(user_id: str):
    """
    A callback function that is used to reload the user object from the user ID stored in the session.

    Args:
        user_id (str): The user ID

    Returns:
        User: The user object
    """
    return User.query.get(uuid.UUID(user_id))

class User(UserMixin, db.Model):
    """
    Represents a user in the system. Each instance of a user is stored in the 'users' table of the database

    Attributes:
        id (UUID): The unique identifier of the user
        name (str): The name of the user
        email (str): The email of the user
        password (str): The password of the user

    Methods:
        __repr__: Returns a string representation of the user
        to_dict: Returns a dictionary representation of the user
    """

    __tablename__ = "users"
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __repr__(self) -> str:
        """
        Returns a string representation of the user

        Returns:
            str: The string representation of the user
        """
        return f"<User {self.name}>"

    def to_dict(self) -> Dict[str, Union[UUID, str]]:
        """
        Returns a dictionary representation of the user

        Returns:
            Dict[str, Union[UUID, str]]: The dictionary representation of the user
        """
        return {"id": self.id, "name": self.name, "email": self.email}
