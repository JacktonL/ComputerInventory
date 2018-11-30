from app.routes import app
from flask import render_template, request
from .Forms import ComputerForm
from .Classes import Computer
from .Classes import Student
from .Classes import Software
from .Forms import Sort
from .misc import sort
from .Forms import SoftwareForm


@app.route("/computers", methods=['GET', 'POST'])
def computers():
    value = False
    check = False
    sortForm = Sort(request.form)
    computerlist = Computer.objects

    form = ComputerForm(request.form)
    if request.method == 'POST' and form.validate():
        number = form.number.data
        status = form.status.data
        os = form.os.data

        for i in Computer.objects:

            if number == str(i.number):
                i.status = status
                i.os = os
                i.save()
                check = True

        if not check:

            value = [number, status, os]

            newComputer = Computer()

            newComputer.number = number
            newComputer.status = status
            newComputer.os = os
            newComputer.save()

    if request.method == "POST" and not sortForm.validate():
        if sortForm.sortComputer.data == 'num':
            computerlist = sort.sortnumber()
        elif sortForm.sortComputer.data == "stat":
            computerlist = sort.sortstatus()
        else:
            computerlist = sort.sortos()

    return render_template("computers.html", form=form, value=value, computers=computerlist, check=check,
                           sort=sortForm)


@app.route("/computer/<computer>", methods=["GET", "POST"])
def computerpage(computer):

    form = ComputerForm(request.form)
    softform = SoftwareForm(request.form)
    studentlist = []

    for i in Computer.objects:
        temp = i.number
        if temp == computer:
            computerObj = i
            for j in Student.objects:
                temp = computerObj.number
                try:
                    if j.computer.number == str(temp):
                        studentlist.append(j)
                except AttributeError:
                    pass

            if request.method == "POST" and form.validate():
                computerObj.os = form.os.data
                computerObj.status = form.status.data

                computerObj.save()

            if request.method == "POST" and softform.validate():

                new_software = Software()

                new_software.anaconda = softform.anaconda.data
                new_software.python = softform.python.data
                new_software.atom = softform.atom.data

                new_software.save()

                computerObj.software = new_software

                computerObj.save()

            return render_template("computerpage.html", value=computerObj, form=form, students=studentlist,
                                   soft=softform)

    return render_template("error.html")

