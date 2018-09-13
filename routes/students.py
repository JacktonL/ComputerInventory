from routes import app
from flask import render_template, request

from .Classes import Student


@app.route("/students", methods=['GET','POST'])
def students():
    form = Student()
    if request.method == 'POST' and form.validate():
        first_name = form.first_name.data
        last_name = form.last_name.data
    return render_template("students.html", form=form)
