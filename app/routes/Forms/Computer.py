from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField


class ComputerForm(FlaskForm):
    number = StringField("Computer Number")
    status = SelectField('Status', choices=[('work', 'Working'), ('bad', 'Not Working')])
    os = SelectField('Operating System', choices=[('lin', 'Linux'), ('win', 'Windows'), ('mac', 'OS X')])
    submit = SubmitField("Submit")
