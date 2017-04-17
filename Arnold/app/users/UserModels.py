from werkzeug import generate_password_hash, check_password_hash
from sqlalchemy import func
from flask_login import UserMixin
from ..common.helpers import JsonSerializer, get_current_time
from .. extensions import db
import UserConstants

class UserJsonSerializer(JsonSerializer):
    """ Deserialize an instance of user model to Json format. """ 

    __json_public__ = ['id', 'email', 'user_name']
    __json_modifiers__ = {
        'role_code' : ['role', (lambda code: UserConstants.USER_ROLE[code])]
    }

class User(db.Model, UserMixin, UserJsonSerializer):
    """ Define User model to correspond with User table. """ 

    __tablename__ = 'user'
    def __repr__(self):
        return '<User %r>' % (self.user_name)

    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(UserConstants.STRING_LEN), nullable = False)
    last_name = db.Column(db.String(UserConstants.STRING_LEN), nullable = False)
    user_name = db.Column(db.String(UserConstants.STRING_LEN), unique = True, nullable = False)
    email = db.Column(db.String(UserConstants.STRING_LEN), unique = True, nullable = False)
    twit_token = db.Column(db.String(UserConstants.TOKEN_LEN), unique = True)
    inst_token = db.Column(db.String(UserConstants.TOKEN_LEN), unique = True)
    redd_token = db.Column(db.String(UserConstants.TOKEN_LEN), unique = True)
    created_on = db.Column(db.DateTime, nullable = False, default = get_current_time)
    role_code = db.Column(db.SmallInteger, default = UserConstants.USER, nullable = False)    

    # User password hashing and storage
    _password = db.Column('password', db.String(UserConstants.PW_STRING_LEN), nullable = False)

    def _get_password(self):
        """ Return user password. """ 
        return self._password

    def _set_password(self, password):
        """ Hash user password so it is never stored as a string. """
        self._password = generate_password_hash(password)

    password = db.synonym('_password',
                            descriptor = property(_get_password, _set_password))

    def check_password(self, password): 
        """ Check password against salted and hashed password value. """
        if self.password is None:
            return False
        return check_password_hash(self.password, password)

    # Other User class methods
    @classmethod
    def authenticate(cls, user_name, password):
        """ Authenticate a user with their username and password. """ 
        user = User.query.filter(db.or_(func.lower(User.user_name) == func.lower(user_name))).first()
        
        if user:
            authenticated = user.check_password(password)
        else:
            authenticated = False
        return user, authenticated    

    @classmethod
    def is_user_name_taken(cls, user_name):
        """ Check if a user with this username already exists. """
        return db.session.query(db.exists().where(func.lower(User.user_name) == func.lower(user_name))).scalar()

    @classmethod
    def is_email_taken(cls, email_address):
        """ Check if a user with this email already exists. """
        return db.session.query(db.exists().where(func.lower(User.email) == func.lower(email_address))).scalar()



