from app.routes import app
from flask import render_template
from .Classes import Student


@app.route("/period")
def period():

    return render_template("period.html", value=Student.objects)
