from time import strftime
from datetime import datetime, date, timedelta
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, RadioField, SelectField, \
    DateField, TextAreaField, FieldList, FormField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError


# from LucasNguyenFIA2DIGI.routes import get_db_connection

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")


class SwapForm(FlaskForm):
    register = SubmitField("Dont have an account? Register Here")


class RoleForm(FlaskForm):
    student = SubmitField("I am a student")
    staff = SubmitField("I am a staff member")


class StudentRegisterForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6, max=30)])
    password_confirm = PasswordField("Confirm Password",
                                     validators=[DataRequired(), Length(min=6, max=30), EqualTo('password')])
    first_name = StringField("First Name", validators=[DataRequired(), Length(min=2, max=55)])
    last_name = StringField("Last Name", validators=[DataRequired(), Length(min=2, max=55)])
    house = SelectField('House',
                        choices=[('B', 'Boek'), ('S', 'Scudo'), ('T', 'Taja'), ('G', 'Gladius'), ('M', 'Mitre')])
    tutor = SelectField('Tutor Number',
                        choices=[('01', '1'), ('02', '2'), ('03', '3'), ('04', '4'), ('05', '5'), ('06', '6'),
                                 ('07', '7'), ('08', '8'), ('09', '9')])
    year = SelectField('Year Level',
                       choices=[('07', '7'), ('08', '8'), ('09', '9'), ('10', '10'), ('11', '11'), ('12', '12')])
    submit = SubmitField("Register Now")

class StaffRegisterForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6, max=30)])
    password_confirm = PasswordField("Confirm Password",
                                     validators=[DataRequired(), Length(min=6, max=30), EqualTo('password')])
    first_name = StringField("First Name", validators=[DataRequired(), Length(min=2, max=55)])
    last_name = StringField("Last Name", validators=[DataRequired(), Length(min=2, max=55)])
    house = SelectField('House',
                        choices=[('B', 'Boek'), ('S', 'Scudo'), ('T', 'Taja'), ('G', 'Gladius'), ('M', 'Mitre')])
    tutor = SelectField('Tutor Number',
                        choices=[('01', '1'), ('02', '2'), ('03', '3'), ('04', '4'), ('05', '5'), ('06', '6'),
                                 ('07', '7'), ('08', '8'), ('09', '9')])
    staffcode = StringField("Staff Code", validators=[DataRequired(), Length(min=2, max=3)])
    submit = SubmitField("Register Now")

class FilterForm(FlaskForm):
    # area = RadioField('Area', choices=[('House','House'),('Tutor','Tutor'),('Student','Student')])
    # Date1 = parameterList[0] Copied to ensure I tackle every spot possible
    # Date2 = parameterList[1]
    # HouseCode = parameterList[2]
    # TutorCode = parameterList[3]
    # GroupBy = parameterList[4]
    # OrderBy = parameterList[5]
    # OrderType = parameterList[6]
    # Select = parameterList[7]
    date1 = DateField('From Date:', default=datetime.strptime('2019/01/01', '%Y/%m/%d'))
    date2 = DateField('To Date:', default=datetime.strptime('2030/01/01', '%Y/%m/%d'))
    area = SelectField('Area', choices=[('School'), ('House'), ('Tutor')])
    house = SelectField('House', choices=[('NOT NULL', ''), ('"B"', 'Boek'), ('"S"', 'Scudo'), ('"T"', 'Taja'),
                                          ('"G"', 'Gladius'),
                                          ('"M"', 'Mitre')])
    tutor = SelectField('Tutor', choices=[('NOT NULL', ''), ('"01"', '1'), ('"02"', '2'), ('"03"', '3'), ('"04"', '4'),
                                          ('"05"', '5'), ('"06"', '6'), ('"07"', '7'), ('"08"', '8'), ('"09"', '9')])
    display = SelectField("Display:", choices=[('s.name', 'Students'), ('SUBSTR(s.tutorCode,1,10)', 'Tutors'),
                                               ('SUBSTR(s.tutorCode,1,1)', 'Houses')])
    order = SelectField("Order", choices=[('DESC', 'Descending'), ('ASC', 'Ascending')])
    filter = SubmitField("Filter")
    reset = SubmitField("Reset")


class CreateForm(FlaskForm):
    students = TextAreaField("List every participating student's student id, by line", validators=[DataRequired()])
    details = StringField("Details", validators=[DataRequired()])
    imageproof = StringField("Please provide a onedrive link of image proof", validators=[DataRequired()])
    housepoints = IntegerField("House Points for activity", validators=[DataRequired()])
    date = DateField("When was this activity Performed?", default=date.today())
    submit = SubmitField("Submit")

class EventForm(FlaskForm):
    student = StringField("Student Id To Search")
    submit = SubmitField("Search")
#
# class ConfirmForm(FlaskForm):
#     confirm = SubmitField("+")
#     delete = SubmitField("-")
#
#
# class EventConfirmForm(FlaskForm):
#     confirm = FieldList(FormField(ConfirmForm), min_entries=4, max_entries=8)
#
#

