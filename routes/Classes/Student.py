from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from mongoengine import Document


class StudentForm(FlaskForm):
    first_name = StringField("Students First Name")
    last_name = StringField('Students Last Name')
    submit = SubmitField("Submit")


class Student(Document):
    first_name = StringField()
    last_name = StringField()
    period = StringField()




