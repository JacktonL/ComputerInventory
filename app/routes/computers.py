from app.routes import app
from flask import render_template, request
from .Forms import ComputerForm
from .Classes import Computer


@app.route("/computers", methods=['GET', 'POST'])
def computers():
    value = False
    check = False
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

    return render_template("computers.html", form=form, value=value, computers=Computer.objects, check=check)


@app.route("/computer/<computer>", methods=["GET", "POST"])
def computerpage(computer):

    for i in Computer.objects:
        temp = i.number
        print(temp)
        if temp == computer:
            computerObj = i
            return render_template("computerpage.html", value=computerObj)

    return render_template("error.html")

