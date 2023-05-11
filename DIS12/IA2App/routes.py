from flask import request, redirect, url_for, flash, session, render_template
from DIS12.IA2App import app
from DIS12.IA2App.forms import LoginForm, RegisterForm, SearchForm
from DIS12.IA2App.apifunctions import search_albums
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

def db_connect():
    connection = sqlite3.connect(r'C:\Users\Lucas Nguyen\PycharmProjects\11DIS\DIS12\IA2App\ndjdatabase.db ')
    return connection
@app.route("/", methods=['GET', 'POST'])
@app.route("/index", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def index():
    form = SearchForm()
    if form.validate_on_submit():
        data = search_albums(form.album.data)
    else:
        data = ['None']

    # return "<h1>Hello Everyone!!</h>"
    return render_template("index.html", login=False, index=True, form=form, data=data)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        conn = db_connect()
        users = conn.execute(f"SELECT FROM users email, password WHERE email = ?" (email))
        conn.close()
        if password == users['password']:
            flash("You have successfully logged in! Good work.")
        return redirect("/index")
    else:
            flash(f"Sorry, there was an error.", "danger")
    return render_template("login.html", form=form, login=True)
@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        password = generate_password_hash(password,"sha256")
        first_name = form.first_name.data
        last_name = form.last_name.data
        conn = db_connect()
        conn.execute("INSERT INTO users (first_name, last_name, email, password) VALUES (?,?,?,?)",
            (first_name, last_name, email, password)
                )
        conn.commit()
        conn.close()
        flash(f"{first_name[1:first_name.length()-1]}, the registration was successful", "success")
        return redirect("/index")
    return render_template("register.html", login=False, registers=True, form=form)

@app.route("/friends", methods=['GET', 'POST'])
def friends():


    return render_template("friends.html", login=False, friends=True)
@app.route("/songs", methods=['GET', 'POST'])
def songs():


    return render_template("songs.html", login=False, songs=True)
