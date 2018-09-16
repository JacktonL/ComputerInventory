from mongoengine import *


class Computer(Document):
    number = StringField()
    status = StringField()
    os = StringField()




