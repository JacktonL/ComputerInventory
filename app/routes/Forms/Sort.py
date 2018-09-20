from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField


class Sort(FlaskForm):
    sortComputer = SelectField("Sort by: ", choices=[('num', 'Number'), ('stat', 'Status'), ('os', "Operating System")])
    sortStudent = SelectField("Sort by: ", choices=[('per', 'Period'), ('name', 'Name')])
    submit = SubmitField("Sort")
