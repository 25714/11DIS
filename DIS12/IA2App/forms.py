from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6,max=30)])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Login")

class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(),Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6,max=30)])
    password_confirm = PasswordField("Confirm Password", validators=[DataRequired(), Length(min=6,max=30), EqualTo('password')])
    first_name = StringField("First Name", validators=[DataRequired(), Length(min=2,max=55)])
    last_name = StringField("Last Name", validators=[DataRequired(), Length(min=2,max=55)])
    submit = SubmitField("Register Now")
    # def validate_password(self,password,password_confirm):
    #     if password!=password_confirm:
    #         raise ValidationError("The password does not match")


class SearchForm(FlaskForm):
    album = StringField("Search Artist", validators=[DataRequired()])
    submit = SubmitField("Search")

class FaveSongNoCap(FlaskForm):
