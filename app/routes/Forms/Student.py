from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class StudentForm(FlaskForm):
    first_name = StringField("Students First Name")
    last_name = StringField('Students Last Name')
    period = StringField('Period #')
    submit = SubmitField("Submit")
