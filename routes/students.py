from routes import app
from flask import render_template, request

from .Classes import Student, StudentForm


@app.route("/students", methods=['GET','POST'])
def students():
    form = StudentForm()
    if request.method == 'POST' and form.validate():
        first_name = form.first_name.data
        last_name = form.last_name.data
        Student.first_name = first_name
        Student.last_name = last_name
    return render_template("students.html", form=form)
