#!/usr/bin/python3

from flask import (
        Flask,
        session,
        render_template,
        redirect,
        url_for,
        escape,
        request
        )

app=Flask(__name__)
app.secret_key = "any random string"

## If the user hits the root of our API
@app.route("/")
def index():
    if "usename" in session:
        username = session["username"]
        return "Logged in as" + username + "<br>" + \
                "<b><a href = '/logout'> click here to log out</a></b>"
    # if the key "username" does nto have a value in session:
    return "Youa re not logged in <br><a href = '/login'></b>" + \
            "click here to log in </b></a>"

@app.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        session["username"] = request.form.get("username")
        return redirect(url_for("index"))

    return """
        <form action = "" method = "post">
            <p><input type = text name = username></p>
            <p><input type = submit value = Login></p>
        </form>
    """

@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port=2224)
