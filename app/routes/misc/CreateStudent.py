from mongoengine import *
from app.routes.Classes.Student import Student


def findstudent(data):

    for i in Student.objects:

        if i.app_id == data['id']:
            return None

    createstudent(data)


def createstudent(data):

    student = Student()

    student.full_name = data["displayName"]
    student.app_id = data["id"]
    student.email = data["emails"][0]["value"]

    student.save()