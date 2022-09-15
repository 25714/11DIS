from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
class RomanForm(FlaskForm):
    roman = IntegerField('Please input a number between 1-3999', validators=[DataRequired()])
    submit = SubmitField("Calculate")
class PSRLSForm(FlaskForm):
    paper = SubmitField(" ")
    scissors = SubmitField(" ")
    rock = SubmitField(" ")
    lizard = SubmitField(" ")
    spock = SubmitField(" ")
    reset = SubmitField("Restart")
class IsomorphForm(FlaskForm):
    string1 = StringField("Please input the first word", validators=[DataRequired()])
    string2 = StringField("Please input the second word", validators=[DataRequired()])
    submit = SubmitField("Check")




