from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config

# Initialize the database
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    # Initialize the database with the app
    db.init_app(app)

    # Import and register the Blueprint
    from routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
