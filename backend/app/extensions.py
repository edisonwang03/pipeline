from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Create a new instance of the SQLAlchemy class. This object will be used to interact with the database.
db = SQLAlchemy()

# Create a new instance of the LoginManager class. This object will be used to manage user authentication.
login_manager = LoginManager()


