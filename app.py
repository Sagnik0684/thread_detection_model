from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from routes import initialize_routes
import config

app = Flask(__name__)
app.config.from_object(config)

# Initialize Database
db = SQLAlchemy(app)

# Initialize Routes
initialize_routes(app)

if __name__ == "__main__":
    app.run(debug=True)
