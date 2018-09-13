from routes import app
from flask import render_template


@app.route("/period")
def period():

    return render_template("period.html")
