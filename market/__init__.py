import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# Create a Flask app
app = Flask(__name__)

# Get absolute path for the database file inside 'instance/' folder
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DB_PATH = os.path.join(BASE_DIR, "instance", "market.db")

# Configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_PATH}"

# Set the secret key to a sufficiently random value
app.config["SECRET_KEY"] = "d901ac455187f7609a9c26c8"

# Configure SQLAlchemy to not track modifications (helps with performance)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize the database
db = SQLAlchemy(app)
# app.app_context().push()

# # Import the routes after the app and db have been initialized
# from market import routes

# Ensure app context is pushed before importing routes
with app.app_context():
    from market import routes
