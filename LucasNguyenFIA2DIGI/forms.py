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


