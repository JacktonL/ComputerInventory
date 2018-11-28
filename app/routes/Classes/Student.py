from mongoengine import *
from .Computer import Computer


class Student(Document):

    full_name = StringField()
    id = StringField()
    period = StringField()
    computer = ReferenceField(Computer)




