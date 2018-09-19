from app.routes import app
from flask import render_template, request
from .Forms import StudentForm
from .Classes import Student
from .Classes import Computer


@app.route("/students", methods=['GET', 'POST'])
def students():
    value = False
    form = StudentForm(request.form)
    print(request.method)
    print(form.validate())
    if request.method == 'POST' and not form.validate():
        print(1)
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



