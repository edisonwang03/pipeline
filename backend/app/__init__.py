from flask import Flask

from config import Config
from app.extensions import db

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Initialize Flask extensions here
    db.init_app(app)
    
    # Register blueprints here
    
    @app.route('/test/')
    def test_page():
        return '<h1>Testing my Flask application</h1>'

    return app