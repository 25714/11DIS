from LucasNguyenFIA2DIGI import app
from flask import request, redirect, url_for, flash, session
from LucasNguyenFIA2DIGI.forms import LoginForm, RegisterForm, FilterForm
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
    Select = parameterList[7]
    NameList = ["House", "Tutor", "Points"]
    leaderboard = conn.execute(f"SELECT {Select}, Events e WHERE SUBSTR(s.TutorCode,2,10) IS {TutorCode} AND e.Date BETWEEN '2019-01-01' AND '2024-01-01' AND e.StudentId = s.StudentId AND SUBSTR(s.TutorCode,1,1) IS {HouseCode} GROUP BY {GroupBy} Order BY {OrderBy} {OrderType}",
                               ()).fetchall()
    conn.close()
    if leaderboard is None:
        abort(404)
    return leaderboard, NameList


###################
# GET ALL
# @api.route('/api', '/api/')
# class GetAndPost(Resource):
#     def get(self):
#         return jsonify(User.objects.all())
#
#     # POST
#     def post(self):
#         data = api.payload
#         user = User(user_id=data['user_id'], email=data['email'], first_name=data['first_name'],
#                     last_name=data['last_name'])
#         user.set_password(data['password'])
#         user.save()
#         return jsonify(User.objects(user_id=data['user_id']))
#
#     # GET ONE
# @api.route('/api/<idx>')
# class GetUpdateDelete(Resource):
#     def get(self, idx):
#         return jsonify(User.objects(user_id=idx))
#
#     # PUT
#     def put(self, idx):
#         data = api.payload
#         User.objects(user_id=idx).update(**data)
#         return jsonify(User.objects(user_id=idx))
#
#     def delete(self, idx):
#         data = api.payload
#         User.objects(user_id=idx).delete()
#         return jsonify(f"User {idx} is deleted")

###################
@app.route("/", methods=['GET', 'POST'])
@app.route("/index", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def index():
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
        leaderboard = filter_points([date1,date2,houseCode,tutorCode,groupBy, "SUM(e.Housepoints)", orderBy,"s.Name StudentName, SUBSTR(s.tutorCode,1,10) Tutor, SUM(e.Housepoints) Points FROM Students s"])
    else:
        leaderboard = filter_points(None)
    return render_template("index.html", login=False, index=True, leaderboard=leaderboard[0], nameList=leaderboard[1], form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if session.get('user_id'):
        flash("You are already logged in.", "danger")
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE email = ?', (email,)).fetchone()
        conn.close()
        if user and user['password'] == password:
            flash(f"{user['first_name']}, you are successfully logged in!", "success")
            session['user_id'] = user['user_id']
            session['username'] = user['first_name']
            return redirect("/index")
        else:
            flash(f"Sorry, there was an error.", "danger")
    return render_template("login.html", title="Login", form=form, login=True)


@app.route("/logout")
def logout():
    session['user_id'] = False
    session['username'] = False
    return redirect(url_for('index'))


@app.route("/register", methods=['GET', 'POST'])
def register():
    if session.get('user_id'):
        flash("You are already logged in.", "danger")
        return redirect(url_for('index'))
    form = RegisterForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        conn = get_db_connection()
        conn.execute("INSERT INTO users (first_name, last_name, email, password) VALUES (?,?,?,?)",
                     (first_name, last_name, email, password)
                     )
        conn.commit()
        conn.close()
        flash(f"{first_name}, you are successfully registered!", "success")
        return redirect(url_for('index'))
    return render_template("register.html", title="Register", register=True, form=form)

# @app.route("/api/<idx>")
# def api(idx = None):
#     if (idx == None):
#         jdata = coursesData
#     else:
#         jdata = coursesData[int(idx)]
#     return Response(json.dumps(jdata), mimetype="FlaskApp1/json")
