from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,ValidationError,BooleanField
from wtforms.validators import InputRequired,Email,EqualTo,Length
from wtforms import ValidationError


# login form
class LoginForm(FlaskForm):
    email = StringField('Your email address',validators=[InputRequired(),Email()])
    password = StringField('Your password',validators=[InputRequired()])
    rememberMe = BooleanField('Remember')
    submit = StringField('Sign In ')