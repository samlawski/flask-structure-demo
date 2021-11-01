from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, EqualTo

class RegisterForm(FlaskForm):
  email = StringField('Email', validators=[DataRequired()])
  password = PasswordField('Password', validators=[DataRequired()])
  password2 = PasswordField(
    'Repeat Password', validators=[DataRequired(), EqualTo('password')]
  )
  submit = SubmitField('Register')

class LoginForm(FlaskForm):
  email = StringField('Email', validators=[DataRequired()])
  password = PasswordField('Password', validators=[DataRequired()])
  submit = SubmitField('Login')