from app.routes import app
from flask import render_template
from .Classes import Student
from .misc import sortname


@app.route("/period")
def period():

    return render_template("period.html", value=Student.objects)


@app.route("/period/<num>", methods=["GET", "POST"])
def periodpage(num):

    student_list = []

    for i in Student.objects:

        if i.period == str(num):

            student_list.append(i)

    return render_template("periodpage.html", value=sortname(student_list), period=num)


