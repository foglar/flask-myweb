from turtle import title
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/projects/solar-sys")
def solarSys():
    return render_template("solar-system.html")

app.run(host='0.0.0.0', port='80', debug=True)