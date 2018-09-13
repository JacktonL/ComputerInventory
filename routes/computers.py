from routes import app
from flask import render_template


@app.route("/computers")
def computers():

    return render_template("computers.html")
