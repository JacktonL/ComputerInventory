from app.routes import app
from flask import render_template, request
from .Forms import StudentForm
from .Classes import Student


@app.route("/students", methods=['GET', 'POST'])
def students():
    value = False
    form = StudentForm(request.form)
    if request.method == 'POST' and form.validate():
        first_name = form.first_name.data
        last_name = form.last_name.data
        period = form.period.data

        value = [first_name, last_name, period]

        newStudent = Student()

        newStudent.first_name = first_name
        newStudent.last_name = last_name
        newStudent.period = period
        newStudent.save()

    return render_template("students.html", form=form, value=value, students=Student.objects)


@app.route("/<student_name>")
def studentpage(student_name):

    for i in Student.objects:
        temp = i.first_name + i.last_name
        if temp == student_name:
            name = i.first_name + " " + i.last_name
            return render_template("studentpage.html", name=name)

    return render_template("error.html")
