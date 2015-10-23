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

class LoginForm(Form):
    l_email = EmailField('Email', [Email()])
    l_password = PasswordField('Password', [Required(), Length(6)])
    submit = SubmitField('Log In')

    def validate(self):
        if not Form.validate(self):
            return False
        
        user = User.query.filter_by(email=self.l_email.data).first()
        if user is None:
            self.l_email.errors.append('User with email %s not registered' % self.l_email.data)
            return False
        if not check_password_hash(user.password, self.l_password.data):
            self.l_password.errors.append('Password is invallid')
            return False
        return True