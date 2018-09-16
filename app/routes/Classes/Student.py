from mongoengine import *
from .Computer import Computer


class Student(Document):
    first_name = StringField()
    last_name = StringField()
    period = StringField()
    computer = ReferenceField(Computer)




