from flask_wtf import FlaskForm
from wtforms import BooleanField, TextField, HiddenField, PasswordField, DateTimeField, IntegerField, SubmitField
from wtforms import validators
import UserConstants

class LoginForm(FlaskForm):
    """ Setup user login form and validators. """
    login = TextField('user_name', [validators.Required()])
    password = TextField('password', [validators.Required()])
    remember_me = BooleanField('remember_me', default = False)

class SignupForm(FlaskForm):
    """ Setup user registration form and validators. """
    first_name = TextField('first_name', [validators.Required()])
    last_name = TextField('last_name', [validators.Required()])
    email = TextField('email', [validators.Required(), validators.Email()])

    user_name = TextField('user_name',[
        validators.Length(
            min = UserConstants.MIN_USERNAME_LEN,
            max = UserConstants.MAX_USERNAME_LEN),
        validators.Regexp(
            "^[a-zA-Z0-9]*$",
            message = "Username may only contain letters and numbers.")])
    
    password = PasswordField(
        'New Password',
        [validators.Length(
            min = UserConstants.MIN_PASSWORD_LEN,
            max = UserConstants.MAX_PASSWORD_LEN)])

    confirm = PasswordField(
        'Repeat Password', [
            validators.Required(),
            validators.EqualTo(
                'password',
                message = 'Passwords must match.')])
