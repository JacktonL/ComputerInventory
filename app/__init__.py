
from mongoengine import *
from flask import Flask

app = Flask(__name__)
app.config["SECRET_KEY"] = "abc"
connect("computerinv", host="mongodb://admin:Hugabuga3@ds149672.mlab.com:49672/computerinv")

from .routes import *
