#!/usr/bin/env python3
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/scoretest/<int:score>")
def hello_name(score):
    return render_template("highscore.html", marks = score)


@app.route("/<username>")
def index(username):
    return render_template("hellobasic.html", name = username)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port = 2224, debug=True)



