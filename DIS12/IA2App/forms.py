from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, SelectField, DateField, TextAreaField, TimeField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6,max=30)])
    dj = BooleanField("I am a DJ")
    submit = SubmitField("Login")

class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(),Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6,max=30)])
    password_confirm = PasswordField("Confirm Password", validators=[DataRequired(), Length(min=6,max=30), EqualTo('password')])
    first_name = StringField("First Name", validators=[DataRequired(), Length(min=2,max=55)])
    last_name = StringField("Last Name", validators=[DataRequired(), Length(min=2,max=55)])
    dob = DateField("Date of Birth", validators=[DataRequired()])
    submit = SubmitField("Register Now")
    # def validate_password(self,password,password_confirm):
    #     if password!=password_confirm:
    #         raise ValidationError("The password does not match")


class SearchForm(FlaskForm):
    album = StringField("Search Artist", validators=[DataRequired()])
    submit = SubmitField("Search")
    category = SelectField('Find',
                        choices=[('Track', 'Track'), ('Album', 'Album'), ('Artist', 'Artist')])

class FaveForm(FlaskForm):
    favourite = SubmitField("Lava U")

class FriendForm(FlaskForm):
    friendId = IntegerField("Friend ID", validators=[DataRequired()])
    submit = SubmitField("Friend!")

class EventForm(FlaskForm):
    location = StringField("Location")
    private = BooleanField("Private?")
    details = TextAreaField("Details")
    dj = IntegerField("DJ ID")
    date = DateField("Date")
    start_time = TimeField("Start Time")
    end_time = TimeField("End Time")
    submit = SubmitField("Submit")

class DjForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    genre = StringField("Main Genre")
    age = IntegerField("Age")
    description = TextAreaField("Description. Sell yourself!")
    price = StringField("A General price per session")
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6,max=30)])
    password_confirm = PasswordField("Confirm Password", validators=[DataRequired(), Length(min=6,max=30), EqualTo('password')])
    submit = SubmitField("Submit")
class RTypeForm(FlaskForm):
    dj = SubmitField("I am a DJ!")
    register = SubmitField("I am a PartyGoer!")

class AForm(FlaskForm):
    search = StringField("Search Artist")
    submit = SubmitField()

class SearchDjForm(FlaskForm):
    name = StringField("Search DJ name")
    genre = StringField("Genre")
    submit = SubmitField("Search!")

class HistoryForm(FlaskForm):
    location = StringField("Search Location")
    submit = SubmitField("Search")

