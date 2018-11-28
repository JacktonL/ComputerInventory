from mongoengine import *
from .Computer import Computer


class Student(Document):

    full_name = StringField()
    app_id = StringField()
    email = StringField()
    period = StringField()
    computer = ReferenceField(Computer)




