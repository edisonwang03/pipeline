import uuid
from typing import Dict, Union

from app.extensions import db
from flask_login import UserMixin
from sqlalchemy.dialects.postgresql import UUID

class User(UserMixin, db.Model):
    """
    Represents a user in the system. Each instance of a user is stored in the 'users' table of the database

    Attributes:
        email (str): The email of the user. This is the primary key of the table
        password (str): The password of the user
        name (str): The name of the user

    Methods:
        __repr__: Returns a string representation of the user
        to_dict: Returns a dictionary representation of the user
    """

    __tablename__ = "users"
    email = db.Column(db.String(100), primary_key=True)
    password = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(100), nullable=False)

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
            Dict[str, str]: The dictionary representation of the user
        """
        return {"name": self.name, "email": self.email}
