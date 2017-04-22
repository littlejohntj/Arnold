from flask_script import Manager, Shell, Server
from flask import current_app
from app import create_app
from app.extensions import db
from app.config import DefaultConfig
import app.models as Models
import os

def create_my_app(config=DefaultConfig):
    """ Create instance of app. """
    return create_app(config)

manager = Manager(create_my_app)

# Runs Flask dev server locally at port 5000 (http://localhost:5000)
manager.add_command("runserver", Server(host = "0.0.0.0", port = 5000))

# Start a Python shell with context of Flask app
@manager.shell
def make_shell_context():
    """ Get app context for resource management. """
    return dict(app = current_app, db = db, models = Models)

# Initialize / reset database
@manager.command
def initdb():
    """ Initialize and reset the app database. """
    db.drop_all(bind = None)
    db.create_all(bind = None)

    # Sample User
    user = Models.User(
        first_name = u'Deborah',
        last_name = u'Venuti',
        user_name = u'Debv',
        password = u'123456',
        email = u'test@test.com')
    db.session.add(user)
    db.session.commit()

if __name__ == '__main__':
    manager.run()
