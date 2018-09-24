from mongoengine import *


class Software(Document):
    anaconda = FloatField()
    python = FloatField()
    atom = StringField()