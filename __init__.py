
from flask_mongoengine import MongoEngine
from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config["SECRET_KEY"] = "abc"
db = MongoEngine(app)
from routes import *
