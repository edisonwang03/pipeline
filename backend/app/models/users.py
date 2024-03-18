from typing import Dict, Union

from app.extensions import db
from flask_login import UserMixin


class User(UserMixin, db.Model):
    """
    Represents a user in the system. Each instance of a user is stored in the 'users' table of the database

    Attributes:
        id (str): The unique identifier of the user
        email (str): The email of the user. This is the primary key of the table
        password (str): The password of the user
        name (str): The name of the user

    Methods:
        __repr__: Returns a string representation of the user
        to_dict: Returns a dictionary representation of the user
    """

    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(100), nullable=False)

    def __repr__(self) -> str:
        """
        Returns a string representation of the user

        Returns:
            str: The string representation of the user
        """
        return f"<User {self.name}>"

    def to_dict(self) -> Dict[str, Union[int, str]]:
        """
        Returns a dictionary representation of the user

        Returns:
            Dict[str, Union[int,str]]: The dictionary representation of the user
        """
        return {"id": self.id, "name": self.name, "email": self.email}
