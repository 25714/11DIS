from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from FIApp1.routes import get_db_connection

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

    def validate_email(self,email):
        conn = get_db_connection()
        conn.execute('SELECT email posts (title, content) VALUES (?, ?)',
                        (title, content))
        conn.commit()
        conn.close()
        if user:
            raise ValidationError("This email is already in use. Please pick another one")

class CalculatorForm(FlaskForm):
    eq = StringField("Please Input an Equation", validators=[DataRequired()])
    submit = SubmitField("Calculate")

class ScoreForm(FlaskForm):
    AddScore1 = SubmitField("Team 1 Goal")
    AddPoint1 = SubmitField("Team 1 Point")
    AddScore2 = SubmitField("Team 2 Goal")
    ResetScore = SubmitField("Reset Scores")

class WordForm(FlaskForm):
    word = StringField("Please input a word", validators=[DataRequired()])
    submit = SubmitField("Calculate")

class HangmanForm(FlaskForm):
    guess = StringField("Please input a single letter guess", validators=[DataRequired(), Length(min=1, max=1)])
    submit = SubmitField("Guess")
    reset = SubmitField("Reset")
class RomanForm(FlaskForm):
    roman = IntegerField('Please input a number between 1-3999', validators=[DataRequired()])
    submit = SubmitField("Calculate")



