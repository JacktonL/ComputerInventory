from mongoengine import *


class Student(Document):
    first_name = StringField()
    last_name = StringField()
    period = StringField()




