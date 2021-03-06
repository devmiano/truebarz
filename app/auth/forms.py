from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,ValidationError,BooleanField
from wtforms.validators import InputRequired,Email,EqualTo,Length
from wtforms import ValidationError
from ..models import User

class RegistrationForm(FlaskForm):
    email = StringField('Your Email Address' ,validators=[InputRequired(), Email()])
    username = StringField('Enter your useraname', validators= [InputRequired()])
    password = PasswordField('Password',validators=[InputRequired(), EqualTo('password_confirm',message ='Password must match')])
    password_confirm = PasswordField('Confirm Password',validators=[InputRequired()])
    submit= SubmitField('Sign Up')

    def validate_email(self,data_field):
        if User.query.filter_by(email = data_field.data).first():
            raise ValidationError('There is an account with that email')
    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('That username is taken')
        
# login form
class LoginForm(FlaskForm):
    username = StringField('Enter username',validators=[InputRequired()])
    password = PasswordField('Your password',validators=[InputRequired()])
    remember = BooleanField('Remember')
    submit = SubmitField('Sign In ')

