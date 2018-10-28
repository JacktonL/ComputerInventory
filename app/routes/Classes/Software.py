from mongoengine import *


class Software(Document):

    softlist = StringField()
    anaconda = FloatField()
    python = FloatField()
    atom = StringField()