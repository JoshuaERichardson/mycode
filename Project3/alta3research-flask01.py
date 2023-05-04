"""
Goal:
At least two endpoints
At least one of your endpoints should return JSON
Has One additional Feature:
    - One endpoint returns HTML that uses jinja2 logic
    - requires a session value be present in order to get a response
    - writes to/reads from a cookie
    - reads from/writes to a sqlite3 database

author: joshuaerichardson
date: 2023-05-04
"""

# import our required libraries
from flask import (
    Flask,
    render_template,
    request,
    session,
    redirect,
    url_for,
    escape,
    jsonify,
)

# create an instance of our Flask app
app = Flask(__name__)

# set up session secret key
app.secret_key = '_5#y2L"F4Q8z\n\xec]/'
session = {}


## create a route for our index page
@app.route("/")
def index():
    if "username" in session:
        return render_template("index.html", data=session["username"])
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
        if (
            request.form["username"] == "admin"
            and request.form["password"] == "password"
        ):
            session["username"] = request.form["username"]
            return redirect(url_for("index"))
        # if the username and password don't match, send the user back to the login page
        else:
            return redirect(url_for("login"))
    # if the user is not logged in, send them to the login page
    else:
        return render_template("login.html")


## create a route for our logout page
@app.route("/logout")
def logout():
    # remove the username from the session if it's there
    session.pop("username", None)
    return redirect(url_for("index"))


## spin up flask
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=2224, debug=True)
