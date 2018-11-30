
from app.routes.Classes import Computer
from app.routes.Classes import Student


def sortstatus():

    valuelist = list("WN")

    sortlist = []

    for i in valuelist:
        for j in Computer.objects:
            if i == j.status[0]:
                sortlist.append(j)

    return sortlist


def sortos():

    valuelist = list("LWO")

    sortlist = []

    for i in valuelist:
        for j in Computer.objects:
            if i == j.os[0]:
                sortlist.append(j)

    return sortlist


def sortnumber():

    sortlist = []

    for i in range(1, 33):
        for j in Computer.objects:
            try:
                if int(j.number) == i:
                    sortlist.append(j)
            except ValueError:
                pass

    return sortlist


def sortperiod():

    sortlist = []

    for i in range(1, 6):

        for j in Student.objects:

            if j.period == str(i):
                sortlist.append(j)

    return sortlist


def sortname(names):

    last = []

    temp = []

    for i in names:

        last.append(i.last_name)

    for i in names:

        for j in sorted(last):

            if i.last_name == j:

                temp.append(i)

    return temp
