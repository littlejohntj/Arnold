from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect

# Instance of Flask-SQLAlchemy extension instance
# Configured with app in app/app.py
db = SQLAlchemy()

# Flask-Login
# Holds the settings used for logging in
login_manager = LoginManager()

# Flask-WTF 
# Global app csrf protection (cross-site request forgery)
csrf = CSRFProtect()





