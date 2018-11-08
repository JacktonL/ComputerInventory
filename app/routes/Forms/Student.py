from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField


class StudentForm(FlaskForm):
    first_name = StringField("Students First Name")
    last_name = StringField('Students Last Name')
    period = SelectField('Period #', choices=[(str(x), x) for x in range(1, 7)])
    submit = SubmitField("Submit")
    assign = SelectField("Assign to Computer: ", choices=[(str(x), x) for x in range(1, 36)])
