"""

Goal:
At least two endpoints  (check)
At least one of your endpoints should return JSON (check)
Has One additional Feature:
    - One endpoint returns HTML that uses jinja2 logic (check)
    - requires a session value be present in order to get a response (check)
    - writes to/reads from a cookie TODO --- skipping
    - reads from/writes to a sqlite3 database (check)

author: joshuaerichardson
date: 2023-05-04

My implementation:
Task list :
    - user name stored in session
    - user tasks stored in cookie
    - list of all users and tasks stored in sqlite3 database
    - one user can have many tasks

    
TODO: Update and Delete tasks
TODO: Modularize our DB into a crud file in models folder
TODO: Push users tasks to cookies for "speed"


"""
############# Imports #####################

# import our required libraries

from flask_bcrypt import Bcrypt
import sqlite3
from flask import Flask, render_template, request, session, redirect, url_for, g
import json


# create an instance of our Flask app
app = Flask(__name__)
bcrypt = Bcrypt(app)

# set up session secret key
app.secret_key = "super secret key"


############# Database #####################

# Database setup:
DATABASE = "./models/users.db"


def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()


def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource("./models/schema.sql", mode="r") as f:
            db.cursor().executescript(f.read())
        db.commit()


# init_db()   <----- run if the db has not been initialized yet

# Database CRUD:


def new_user(username, password):
    with app.app_context():
        connection = get_db()
        cur = connection.cursor()
        print("NEW USER FUNCTION")
        cur.execute(
            "INSERT INTO users (username, hash_password) VALUES (?, ?)",
            (username, password),
        )
        connection.commit()


def insert_task(user_id, task):
    with app.app_context():
        connection = get_db()
        cur = connection.cursor()
        cur.execute("INSERT INTO tasks (user_id, task) VALUES (?, ?)", (user_id, task))
        connection.commit()


def get_every_tasks():
    with app.app_context():
        connection = get_db()
        cur = connection.cursor()
        cur.execute("SELECT * FROM tasks")
        return cur.fetchall()


def get_all_tasks(user_id):
    with app.app_context():
        connection = get_db()
        cur = connection.cursor()
        cur.execute("SELECT task FROM tasks WHERE user_id=?", (user_id, ))
        return cur.fetchall()


def get_user(username):
    with app.app_context():
        connection = get_db()
        cur = connection.cursor()
        cur.execute("SELECT * FROM users WHERE username=?", (username, ))
        return cur.fetchall()


def get_user_name(user_id):
    with app.app_context():
        connection = get_db()
        cur = connection.cursor()
        cur.execute("SELECT username FROM users WHERE id=?", (user_id, ))
        return cur.fetchall()


def check_password(username, passed_password):
    with app.app_context():
        connection = get_db()
        cur = connection.cursor()
        hashed_password = get_user(username)[0][2]
        is_password = bcrypt.check_password_hash(hashed_password, passed_password)
        return is_password


############# Routes #####################


## create a route for our index page
@app.route("/")
def index():
    if "username" in session:
        # Get all tasks for the user
        user_id = session["user_id"]
        tasks = get_all_tasks(user_id)
        return render_template("index.html", data=session["username"], tasks=tasks)
    else:
        return render_template("index.html")


## create a route for our login page
@app.route("/login", methods=["GET", "POST"])
def login():
    # if the user is already logged in, send them to the index page
    if "username" in session:
        return redirect(url_for("index"))
    # if the user is not logged in, grab the form data:
    if request.method == "POST":
        # if the username and password match, log the user in
        username = request.form["username"]
        password = request.form["password"]
        #  check if the username is in the database
        is_user = check_password(username, password)
        # if the username and password match, log the user in
        if is_user:
            session["username"] = request.form["username"]
            session["user_id"] = get_user(username)[0][0]
            return redirect(url_for("index"))
        # if the username and password don't match, send the user back to the login page
        else:
            return redirect(url_for("login"))
    # if the user is not logged in, send them to the login page
    else:
        return render_template("login.html")


## create a route for new user:
@app.route("/newuser", methods=["POST"])
def newuser():
    # Save the username and password from the form
    username = request.form["username"]
    # Hash the password
    pw_hash = Bcrypt().generate_password_hash(request.form["password"]).decode("utf-8")
    # Save the username and hashed password to the database
    new_user(username, pw_hash)
    # Save the username to the session
    session["username"] = username
    session["user_id"] = get_user(username)[0][0]
    # Redirect the user to the index page:
    return redirect(url_for("index"))


## create a route for all_tasks:
@app.route("/all_tasks")
def all_tasks():
    print("ALL TASKS FUNCTION")

    # Grab all the tasks from the database
    tasks = get_every_tasks()

    # Join the tasks with the userame:
    task_list = []
    for task in tasks:
        task_list.append({"username": get_user_name(task[1])[0][0], "task": task[2]})

    # Make task_list into json:
    task_list = json.dumps(task_list)
    return task_list


## create a route for our logout page
@app.route("/logout")
def logout():
    # remove the username from the session if it's there
    session.pop("username", None)
    session.pop("user_id", None)
    return redirect(url_for("index"))


## create a route for a new task:
@app.route("/new_task", methods=["POST"])
def new_task():
    # Save the task from the form
    task = request.form["task"]
    # Save the username from the session
    user_id = session["user_id"]
    # Save the task to the database
    insert_task(user_id, task)
    # Save the task to the cookies:
    ### DISREGARD tasks = request.cookies.get("tasks")
    

    # Redirect the user to the index page:
    return redirect(url_for("index"))


## spin up flask
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
