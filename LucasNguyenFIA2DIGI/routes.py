from LucasNguyenFIA2DIGI import app
from flask import request, redirect, url_for, flash, session
from LucasNguyenFIA2DIGI.forms import LoginForm, StudentRegisterForm, StaffRegisterForm, RoleForm, FilterForm, CreateForm, SwapForm, EventForm
import sqlite3
from flask import render_template, abort


def get_db_connection():
    conn = sqlite3.connect(r'C:\Program Files\SQLiteStudio\SchoolTestDB')
    conn.row_factory = sqlite3.Row
    return conn

def filter_points(parameterList=None):
    if parameterList is None:
        parameterList = ['2019-01-01', '2024-01-01', "NOT NULL", "NOT NULL", "SUBSTR(s.tutorcode,1,10)", "SUM(e.Housepoints)", "Desc", "s.Name StudentName, SUBSTR(s.tutorCode,1,10) Tutor, SUM(e.Housepoints) Points FROM Students s"]
    conn = get_db_connection()
    Date1 = parameterList[0]
    Date2 = parameterList[1]
    HouseCode = parameterList[2]
    TutorCode = parameterList[3]
    GroupBy = parameterList[4]
    OrderBy = parameterList[5]
    OrderType = parameterList[6]
    Select = "s.Name StudentName, SUBSTR(s.tutorCode,1,10) Tutor, SUM(e.Housepoints) Points FROM Students s"
    NameList = ["Name", "Tutor", "Points"]
    if GroupBy == "s.name":
        NameList = ["Name", "Tutor", "Points"]
        Select = "s.Name StudentName, SUBSTR(s.tutorCode,1,10) Tutor, SUM(e.Housepoints) Points FROM Students s"
    if GroupBy == "SUBSTR(s.tutorCode,1,10)":
        NameList = ["Tutor", "Points"]
        Select = "SUBSTR(s.tutorCode,1,10) Tutor, SUM(e.Housepoints) Points FROM Students s"
    if GroupBy == "SUBSTR(s.tutorCode,1,1)":
        NameList = ["House", "Points"]
        Select = "SUBSTR(s.tutorCode,1,1) House, SUM(e.Housepoints) Points FROM Students s"
    leaderboard = conn.execute(f"SELECT {Select}, Events e WHERE SUBSTR(s.TutorCode,2,10) IS {TutorCode} AND e.Date BETWEEN '{Date1}' AND '{Date2}'AND e.StudentId = s.StudentId AND e.confirmedBy IS NOT NULL AND SUBSTR(s.TutorCode,1,1) IS {HouseCode} GROUP BY {GroupBy} Order BY {OrderBy} {OrderType}",
                               ()).fetchall()
    conn.close()
    if leaderboard is None:
        abort(404)
    return leaderboard, NameList

@app.route("/", methods=['GET', 'POST'])
@app.route("/index", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def index():
    session['form'] = False
    session['type'] = False
    # return "<h1>Hello Everyone!!</h>"
    # Date1 = parameterList[0]
    # Date2 = parameterList[1]
    # HouseCode = parameterList[2]
    # TutorCode = parameterList[3]
    # GroupBy = parameterList[4]
    # OrderBy = parameterList[5]
    # OrderType = parameterList[6]
    # Select = parameterList[7]
    form = FilterForm()
    if form.validate_on_submit():
        if form.reset.data:
            return(redirect('/index'))
        date1 = form.date1.data
        date2 = form.date2.data
        houseCode = form.house.data
        tutorCode = form.tutor.data
        groupBy = form.display.data
        orderBy = form.order.data
        conn = get_db_connection()
        conn.close()
        leaderboard = filter_points([date1,date2,houseCode,tutorCode,groupBy, "SUM(e.Housepoints)", orderBy])
    else:
        leaderboard = filter_points(None)
    return render_template("index.html", login=False, index=True, leaderboard=leaderboard[0], nameList=leaderboard[1], form=form)


@app.route("/logout")
def logout():
    session['name'] = False
    session['id'] = False
    session['staff'] = False
    session['type'] = False
    return redirect(url_for('index'))


@app.route("/login", methods=['GET', 'POST'])
def login():
    form2 = SwapForm()
    if session.get('type'):
        type = session['type']
        title = type
        if type == "Student":
            form = StudentRegisterForm()
        if type == "Staff":
            form = StaffRegisterForm()
        if type == "Role":
            form = RoleForm()
            type = 'Role'
            title = "Register"
    else:
        type = "Login" #start page as login page
        title = "Login"
        form = LoginForm()
    if (form.validate_on_submit() or form2.validate_on_submit()) and type == "Login": #If it submits and we are trying to login
        if not form2.register.data: #If they clicked submit
            if form.validate_on_submit(): #This was needed since it kept not actually checking
                email = form.email.data
                password = form.password.data
                if email[0].isalpha(): #If staff
                    conn = get_db_connection()
                    user=conn.execute('SELECT * FROM staff WHERE username = ?', (email.replace('@stpauls.qld.edu.au',''),)).fetchone()
                    conn.close()
                    if user and user['password'] == password: #staff login
                        flash(f"{user['staffname']}, you are successfully logged in!", "success")
                        session['name'] = user['staffname'] #Set staff to logged in
                        session['id'] = user['staffId']
                        session['staff'] = user['houseleader'] + 1
                        session['type'] = False
                        return redirect(url_for('index'))
                    else:
                        flash(f"Sorry, there was an error.", "danger")
                elif email[0].isdigit(): #If staff
                    conn = get_db_connection() #Student Login
                    user= conn.execute('SELECT * FROM students WHERE Studentid = ?', (email[0:5],)).fetchone()
                    conn.close()
                    if user and user['password'] == password:
                        flash(f"{user['name']}, you are successfully logged in!", "success")
                        session['name'] = user['name']
                        session['staff'] = -1
                        session['id'] = user['StudentId'] #set student to logged in
                        session['type'] = False
                        return redirect(url_for('index'))
                    else:
                        flash(f"Sorry, there was an error.", "danger")
                else:
                    flash(f"Sorry, there was an error.", "danger")
        else: #If they clicked Register
            session['type'] = "Role"
            return redirect(url_for('login'))
    if form.validate_on_submit() and type == "Role":
        if form.student.data:
            # flash(f"you, you are successfully registered!", "success")
            type = "Student"
            session['type'] = type
            # flash(f"type, you are successfully registered!", "success")
            return redirect(url_for('login'))
        if form.staff.data:
            type = "Staff"
            session['type'] = type
            return redirect(url_for('login'))
    elif form.validate_on_submit() and type == "Student":
        # flash(f"you, you are successfully registered!", "success")
        email = form.email.data
        password = form.password.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        house = form.house.data
        tutor = form.tutor.data
        year = form.year.data
        conn = get_db_connection()
        conn.execute(f"INSERT INTO students (name, StudentId, password, tutorcode, yearlevel) VALUES (?,?,?,?,?)",
                     (f"{first_name + ' ' + last_name}", email[0:5], password, f"{house+tutor}", year)
                     )
        conn.commit()
        conn.close()
        # title = f"{first_name, last_name}, email[0:5], password, {house + tutor})"
        session['type'] = False
        return redirect(url_for('index'))
        flash(f"You are successfully registered!", "success")
    elif form.validate_on_submit() and type == "Staff":
        email = form.email.data
        password = form.password.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        house = form.house.data
        tutor = form.tutor.data
        staffcode = form.staffcode.data
        houseleader = 0
        conn = get_db_connection()
        conn.execute(f"INSERT INTO staff (Staffname, Username, password, tutorcode, staffid, houseleader) VALUES (?,?,?,?,?,?)",
                     (f"{first_name + ' ' + last_name}", email.replace("@stpauls.qld.edu.au", ""), password, f"{house+tutor}", staffcode.upper(), houseleader))
        conn.commit()
        conn.close()
        # title = f"{first_name, last_name}, email[0:5], password, {house + tutor})"
        session['type'] = False
        flash(f"You are successfully registered!", "success")
        return redirect(url_for('index'))
    # elif form.staff.data:
    #     form = StudentRegisterForm()
    #     type = "Staff"
    #     if form.validate_on_submit():
    #         email = form.email.data
    #         password = form.password.data
    #         first_name = form.first_name.data
    #         last_name = form.last_name.data
    #         conn = get_db_connection()
    #         conn.execute("INSERT INTO users (first_name, last_name, email, password) VALUES (?,?,?,?)",
    #                      (first_name, last_name, email, password)
    #                      )
    #         conn.commit()
    #         conn.close()
    #         flash(f"{first_name}, you are successfully registered!", "success")
    #         return render_template("login.html", title=title, register=True, form=form, type=type)
    return render_template("login.html", title=title, login=True, form=form, type=type, form2=form2)

@app.route("/events", methods=['GET', 'POST'])
def events():
    form = EventForm()
    if form.validate_on_submit():
        studentid = form.student.data
        conn = get_db_connection()
        eventsdata=conn.execute('SELECT StudentId, Setby, ConfirmedBy, Details, ImageProof, HousePoints, Date FROM events WHERE StudentId = ?', (studentid,)).fetchall()
        conn.close()
    else:
        conn = get_db_connection()
        eventsdata=conn.execute('SELECT StudentId, Setby, ConfirmedBy, Details, ImageProof, HousePoints, Date FROM events WHERE StudentId = ?', (session['id'],)).fetchall()
        conn.close()
    eventsList = ["StudentId", "Set By", "Confirmed By", "Details", "Image Proof", "House Points", "Date"]
    return render_template("events.html", title="Events", event=True, eventsdata=eventsdata, eventsList=eventsList, form=form)

# @app.route("/api/<idx>")
# def api(idx = None):email = StringField("Email", validators=[DataRequired(), Email()])
#     password = PasswordField("Password", validators=[DataRequired(), Length(min=6, max=30)])
#     password_confirm = PasswordField("Confirm Password",validators=[DataRequired(), Length(min=6, max=30), EqualTo('password')])
#     first_name = StringField("First Name", validators=[DataRequired(), Length(min=2, max=55)])
#     last_name = StringField("Last Name", validators=[DataRequired(), Length(min=2, max=55)])
#     house = SelectField('House', choices=[('"B"', 'Boek'), ('"S"', 'Scudo'), ('"T"', 'Taja'), ('"G"', 'Gladius'),('"M"', 'Mitre')])
#     tutor = SelectField('Tutor Number', choices=[('"01"','1'), ('"02"','2'), ('"03"','3'), ('"04"','4'), ('"05"','5'), ('"06"','6'), ('"07"','7'), ('"08"','8'), ('"09"','9')])
#     submit = SubmitField("Register Now")
# class StaffRegisterForm(FlaskForm):
#     if (idx == None):
#         jdata = coursesData
#     else:
#         jdata = coursesData[int(idx)]
#     return Response(json.dumps(jdata), mimetype="FlaskApp1/json")
@app.route("/create", methods=['GET', 'POST'])
def create():
    form = CreateForm()
    if form.validate_on_submit():
        # students = TextAreaField("List every participating student on a new line")
        #     details = StringField("Details")
        #     imageproof = StringField("Please provide a onedrive link of image proof")
        #     housepoints = IntegerField("House Points for activity")
        #     date = DateField("When was this activity Performed?", default=date.today())
        #     submit = SubmitField("Submit")
        students = form.students.data
        details = form.details.data
        imageproof = form.imageproof.data
        housepoints = form.housepoints.data
        date = form.date.data
        setby = session['id']
        conn = get_db_connection()
        for student in students.split():
            conn.execute("INSERT INTO events (StudentId, Setby, details, imageproof, housepoints, date) VALUES (?,?,?,?,?,?)",
                (student , setby, details, imageproof,housepoints,date))
        conn.commit()
        conn.close()
        flash(f"Event Successfully Created!", "success")
        return redirect(url_for("index"))
    return render_template("create.html", title="Create", create=True, form=form)

@app.route("/confirm", methods=['GET', 'POST'])
def confirm():
    conn = get_db_connection()
    events = conn.execute('SELECT eventid, studentid, setby, details, imageproof , housepoints, date FROM events WHERE ConfirmedBy IS NULL').fetchall()
    conn.close()
    if events == None:
        events = ["",""]
    nameList = ["EventId","StudentId", "Set by", "Details", "Image Proof", "House Points", "Date", "Confirm", "Deny"]
    return render_template("confirm.html", title="Create", confirm=True, events=events, nameList=nameList)

@app.route('/<int:eventid>/accept/', methods=('POST','GET'))
def accept(eventid):

    conn = get_db_connection()
    setby = conn.execute('SELECT * FROM events WHERE eventId = ?',(eventid,)).fetchone()
    conn.close()
    if setby['SetBy'] == session['id']:
        flash(f"You may not confirm your own event.", "danger")
    else:
        conn = get_db_connection()
        conn.execute('UPDATE events SET ConfirmedBy = ? WHERE eventid = ? ',(session['id'],eventid, ))
        conn.commit()
        flash(f' Event {eventid} was successfully confirmed')
    conn.close()
    return redirect(url_for("confirm"))



@app.route('/<int:eventid>/delete/', methods=('POST','GET'))
def delete(eventid):

    conn = get_db_connection()
    conn.execute('DELETE FROM events WHERE eventid = ?',(eventid,))
    conn.commit()
    conn.close()
    flash(f' Event {eventid} was successfully deleted!')
    return redirect(url_for("confirm"))
