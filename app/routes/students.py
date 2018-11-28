from app.routes import app
from flask import render_template, request
from .Forms import Sort, StudentForm
from .Classes import Student
from .Classes import Computer
from .misc import sortperiod


@app.route("/students", methods=['GET', 'POST'])
def students():
    value = False
    sortForm = Sort(request.form)
    studentlist = Student.objects

    if request.method == 'POST' and not sortForm.validate():
        if sortForm.sortStudent.data == 'per':
            studentlist = sortperiod()

    return render_template("students.html", value=value, students=studentlist, sort=sortForm)


@app.route("/student/<student>", methods=['GET', 'POST'])
def studentpage(student):

    form = StudentForm(request.form)

    for i in Student.objects:
        temp = i.full_name.replace(" ", "_")
        if temp == student:
            studentObj = i
            if request.method == 'POST' and form.validate():
                studentObj.period = form.period.data
                for i in Computer.objects:
                    if i.number == form.assign.data:
                        studentObj.computer = i
                        studentObj.save()

            return render_template("studentpage.html", form=form, student=studentObj, comp=Computer.objects)

    return render_template("error.html")



