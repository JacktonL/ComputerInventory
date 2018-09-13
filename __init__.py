
from mongoengine import *
from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config["SECRET_KEY"] = "abc"
connect("computerinv")
from routes import *
