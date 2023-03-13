from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, EmailField
from wtforms.validators import DataRequired, EqualTo

class loginForm(FlaskForm):
    username = StringField("Enter your username", validators= [DataRequired()])
    password = PasswordField("Enter a password", validators=[DataRequired()])
    submit = SubmitField("Submit")

class signUpForm(FlaskForm):
    username = StringField("Enter your username", validators=[DataRequired()])
    email = EmailField("Enter your email", validators=[DataRequired()])
    password = PasswordField("Enter a password", validators=[DataRequired()])
    confirmPassword = PasswordField("Confirm password", validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField("Submit")

class gameForm(FlaskForm):
    countryPick = StringField("Country")
    cityPick = StringField("City")
    waterPick = StringField("Water (River/Ocean/etc)")
    mountainPick = StringField("Mountain (Peak/Mountains)")
    cropPick = StringField("Crops/Plants")
    animalPick = StringField("Animal")
    submit = SubmitField("Submit Answers")

class changeEmailForm(FlaskForm):
    email = EmailField("Enter new email", validators=[DataRequired()])
    submit = SubmitField("Change email")

class changePasswordForm(FlaskForm):
    password = PasswordField("Enter new password", validators=[DataRequired()])
    confirmPassword = PasswordField("Confirm password", validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField("Change password")