from app.routes import app
from flask import render_template, request
from .Forms import ComputerForm
from .Classes import Computer
from .Classes import Student
from .Forms import Sort
from .misc import sort


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
        if sortForm.sortComputer.data == 'Number':
            computerlist = sort.sortnumber()
        elif sortForm.sortComputer.data == "Status":
            computerlist = sort.sortstatus()
        else:
            computerlist = sort.sortos()

    return render_template("computers.html", form=form, value=value, computers=computerlist, check=check,
                           sort=sortForm)


@app.route("/computer/<computer>", methods=["GET", "POST"])
def computerpage(computer):
    form = ComputerForm(request.form)
    studentlist = []
    for i in Computer.objects:
        temp = i.number
        print(temp)
        if temp == computer:
            computerObj = i
            for j in Student.objects:
                if j.computer.number == i.number:
                    studentlist.append(j)
            if request.method == "POST" and form.validate():
                computerObj.os = form.os.data
                computerObj.status = form.status.data

                computerObj.save()

            return render_template("computerpage.html", value=computerObj, form=form, students=studentlist)

    return render_template("error.html")

