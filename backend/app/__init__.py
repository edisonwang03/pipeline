from flask import Flask

from config import Config
from app.extensions import db
from app.routes.users import users_bp

from sqlalchemy import text

def create_app(config_class=Config):
    """
    Create a Flask application using the app factory pattern.
    
    Params:
        config_class (Config): The configuration settings to use
        
    Returns:
        app (Flask): A Flask application
    """
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Initialize Flask extensions here
    db.init_app(app)
    
    # Create the database tables
    with app.app_context():
        db.create_all()
    
    # Register blueprints here
    app.register_blueprint(users_bp)

    return app