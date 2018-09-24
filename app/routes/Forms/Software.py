from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField


class SoftwareForm(FlaskForm):
    anaconda = StringField("Anaconda Version: ")
    python = StringField("Python Version: ")
    atom = SelectField("Has Atom? ", choices=[("Yes", "Yes"), ("No", "No")])

