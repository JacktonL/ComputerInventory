from app.routes import app
from flask import render_template, request
from .Forms import StudentForm, Sort
from .Classes import Student
from .Classes import Computer
from .misc import sortperiod



@app.route("/students", methods=['GET', 'POST'])
def students():
    value = False
    form = StudentForm(request.form)
    sortForm = Sort(request.form)
    studentlist = Student.objects

    if request.method == 'POST' and not form.validate() and form.period.data != "":
        if form.first_name.data[-1] == ' ':
            first_name = form.first_name.data[:-1]
        else:
            first_name = form.first_name.data
        if form.last_name.data[-1] == ' ':
            last_name = form.last_name.data[:-1]
        else:
            last_name = form.last_name.data
        if form.period.data[-1] == " ":
            period = form.period.data[:-1]
        else:
            period = form.period.data

        value = [first_name, last_name, period]

        newStudent = Student()

        newStudent.first_name = first_name
        newStudent.last_name = last_name
        newStudent.period = period
        newStudent.save()

    if request.method == 'POST' and not sortForm.validate():
        print(1)
        if sortForm.sortStudent.data == 'per':
            studentlist = sortperiod()

    return render_template("students.html", form=form, value=value, students=studentlist, sort=sortForm)


@app.route("/student/<student>", methods=['GET', 'POST'])
def studentpage(student):

    form = StudentForm(request.form)

    for i in Student.objects:
        temp = i.first_name + i.last_name
        if temp == student:
            studentObj = i
            if request.method == 'POST' and form.validate():
                for i in Computer.objects:
                    if i.number == form.assign.data:
                        studentObj.computer = i
                        studentObj.save()

            return render_template("studentpage.html", form=form, student=studentObj, comp=Computer.objects)

    return render_template("error.html")



