from flask import Flask

from config import Config
from app.extensions import db

from sqlalchemy import text

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Initialize Flask extensions here
    db.init_app(app)
    
    # Register blueprints here
    
    @app.route('/')
    def test_page():
        return '<h1>Testing my Flask application</h1>'
    
    @app.route('/test_db')
    def test_db():
        try:
            db.session.query(text("1")).from_statement(text("SELECT 1")).all()
            return '<h1>It works.</h1>'
        except Exception as e:
            print(e)
            return '<h1>Something is broken.</h1>'

    return app