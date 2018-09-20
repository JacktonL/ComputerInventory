
from app.routes.Classes import Computer


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

            if int(j.number) == i:
                sortlist.append(j)

    return sortlist





