
from mongoengine import *
from flask import Flask

app = Flask(__name__)
app.config["SECRET_KEY"] = "abc"
connect("computerinv")

from .routes import *
