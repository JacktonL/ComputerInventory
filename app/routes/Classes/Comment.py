from mongoengine import *
from datetime import datetime


class Comment(Document):

    first_name = StringField()
    last_name = StringField()
    date = DateTimeField()
    comment = StringField()