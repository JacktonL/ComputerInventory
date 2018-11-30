from mongoengine import *
from datetime import datetime


class Comment(Document):

    full_name = StringField()
    date = StringField()
    comment = StringField()