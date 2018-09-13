
from mongoengine import *
from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config["SECRET_KEY"] = "abc"
connect("computerinv", host="mongodb://admin:Hugabuga3@ds149672.mlab.com:49672/computerinv")
from routes import *
