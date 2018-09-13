from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class Student(FlaskForm):
    first_name = StringField("Students First Name")
    last_name = StringField('Students Last Name')
    submit = SubmitField("Submit")



