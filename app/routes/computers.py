from app.routes import app
from flask import render_template, request
from .Forms import ComputerForm
from .Classes import Computer


@app.route("/computers", methods=['GET', 'POST'])
def computers():
    value = False
    form = ComputerForm(request.form)
    if request.method == 'POST' and form.validate():
        number = form.number.data
        status = form.status.data
        os = form.os.data

        value = [number, status, os]

        newStudent = Computer()

        newStudent.number = number
        newStudent.status = status
        newStudent.os = os
        newStudent.save()
    return render_template("computers.html", form=form, value=value, students=Computer.objects)
