from flask.ext.wtf import Form
from wtforms import TextField, IntegerField, PasswordField, SubmitField, TextAreaField, SelectField
from wtforms.validators import Required, Length, NumberRange,EqualTo, Email
from flask.ext.wtf.html5 import EmailField
from app.models import User
from werkzeug.security import check_password_hash

class SignupForm(Form):
    first_name = TextField('First Name', [Required(), Length(3)])
    last_name = TextField( 'Last Name', [Required(), Length(3)])
    email = TextField('Email', [Email()])
    password = PasswordField('Password', [Required(), Length(6)])
    confirm_password = PasswordField('Confirm password', [EqualTo('password')])
    image_url = TextField('Image URL', [Required()])
    submit = SubmitField('Sign Up')
