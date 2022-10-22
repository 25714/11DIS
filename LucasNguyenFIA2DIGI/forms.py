from time import strftime
from datetime import datetime, date, timedelta
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, RadioField, SelectField, DateField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError


# from LucasNguyenFIA2DIGI.routes import get_db_connection

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6, max=30)])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Login")

class RoleForm(FlaskForm):
    student = SubmitField("I am a student")
    staff = SubmitField("I am a staff member")
class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6, max=30)])
    password_confirm = PasswordField("Confirm Password",validators=[DataRequired(), Length(min=6, max=30), EqualTo('password')])
    first_name = StringField("First Name", validators=[DataRequired(), Length(min=2, max=55)])
    last_name = StringField("Last Name", validators=[DataRequired(), Length(min=2, max=55)])
    teacher_code = StringField("If you are a teacher, please input the Teacher Code")
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
    house = SelectField('House', choices=[('NOT NULL', ''), ('"B"', 'Boek'), ('"S"', 'Scudo'), ('"T"', 'Taja'), ('"G"', 'Gladius'),
                                          ('"M"', 'Mitre')])
    tutor = SelectField('Tutor', choices=[('NOT NULL', ''), ('"01"','1'), ('"02"','2'), ('"03"','3'), ('"04"','4'), ('"05"','5'), ('"06"','6'), ('"07"','7'), ('"08"','8'), ('"09"','9')])
    display = SelectField("Display:", choices=[('s.name','Students'), ('SUBSTR(s.tutorCode,1,10)','Tutors'), ('SUBSTR(s.tutorCode,1,1)','Houses')])
    order = SelectField("Order", choices=[('DESC','Descending'), ('ASC','Ascending')])
    filter = SubmitField("Filter")
    reset = SubmitField("Reset")

    # def validate_email(self,email):
    #     conn = get_db_connection()
    #     conn.execute('SELECT email posts (title, content) VALUES (?, ?)',
    #                     (title, content))
    #     conn.commit()
    #     conn.close()
    #     if user:
    #         raise ValidationError("This email is already in use. Please pick another one")
    #
    #
