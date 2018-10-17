from mongoengine import *
from .Software import Software


class Computer(Document):
    number = StringField()
    status = StringField()
    os = StringField()
    software = ReferenceField(Software)




