#This file imports specific tools that will help us make sure users are giving us the correct information

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Email

class UserLoginForm(FlaskForm):
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    submit_button = SubmitField()