from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField


class ComputerForm(FlaskForm):
    number = StringField("Computer Number")
    status = SelectField('Status', choices=[('Working', 'Working'), ('Not Working', 'Not Working')])
    os = SelectField('Operating System', choices=[('Linux', 'Linux'), ('Windows', 'Windows'), ('OS X', 'OS X')])
    submit = SubmitField("Submit")
