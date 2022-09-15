from FIApp1 import app
from flask import request, redirect, url_for, flash, session
from FIApp1.models import User
from FIApp1.forms import LoginForm, RegisterForm, CalculatorForm, ScoreForm, WordForm, HangmanForm, RomanForm
from FIApp1.calculator import calculator
from FIApp1.hangman import string_writer
from FIApp1.Romannumerals import RomanNumerals
import sqlite3
from flask import render_template, abort

def get_db_connection():
    conn = sqlite3.connect(r'/LucasNguyenFIA2DIGI/database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post


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
@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    # return "<h1>Hello Everyone!!</h>"
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template("index.html", login=False, index=True, posts=posts)

@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        elif not content:
            flash('Content is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
                         (title, content))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
    return render_template('create.html', create=True, title="Create Post")


@app.route('/<int:id>/edit/', methods=('GET', 'POST'))
def edit(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')

        elif not content:
            flash('Content is required!')

        else:
            conn = get_db_connection()
            conn.execute('UPDATE posts SET title = ?, content = ?'
                         ' WHERE id = ?',
                         (title, content, id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('edit.html', post=post)

@app.route('/<int:id>/delete/', methods=('POST',))
def delete(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM users WHERE user_id = ?', (id,))
    conn.commit()
    conn.close()
    flash(f' user {id} was successfully deleted!')
    return redirect(url_for('index'))


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
        user = conn.execute('SELECT * FROM users WHERE email = ?', (email, )).fetchone()
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


@app.route("/courses")
@app.route("/courses/<year>")
def courses(term=None):
    if term is None:
        term = "Spring 2022"
    conn = get_db_connection()
    coursesData = conn.execute('SELECT * FROM courses').fetchall()
    conn.close()
    return render_template("courses.html", courseData=coursesData, courses=True, year=term)


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
            (first_name , last_name, email, password)
                )
        conn.commit()
        conn.close()
        flash(f"{first_name}, you are successfully registered!", "success")
        return redirect(url_for('index'))
    return render_template("register.html", title="Register", register=True, form=form)


@app.route("/enrolment", methods=["GET", "POST"])
def enrolment():
    if not session.get('user_id'):
        flash("You need to log in to access this page.", "danger")
        return redirect(url_for('login'))
    courseID = request.form.get("courseID")
    user_id = session.get('user_id')
    if courseID:
        if request.method == 'POST':
            user_id = session.get('user_id')
            course_id = request.form.get("courseID")
            conn = get_db_connection()
            conn.execute("INSERT INTO enrolment (course_id,user_id) VALUES (?,?)",
                (course_id, user_id)
                )
            conn.commit()
            conn.close()

    conn = get_db_connection()
    classes = conn.execute('SELECT c.course_id, c.title, c.description, c.credits, c.term FROM enrolment AS e INNER JOIN courses as c ON e.course_id = c.course_id WHERE user_id = ?', (user_id, )).fetchall()
    conn.close()
    return render_template("enrolment.html", enrolment=True, title="Enrolment", classes=classes)


# @app.route("/api/")
# @app.route("/api/<idx>")
# def api(idx = None):
#     if (idx == None):
#         jdata = coursesData
#     else:
#         jdata = coursesData[int(idx)]
#     return Response(json.dumps(jdata), mimetype="FlaskApp1/json")
