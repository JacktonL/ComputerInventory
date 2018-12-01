
from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField


class StudentForm(FlaskForm):

    period = SelectField("Choose Period", choices=[(str(x), str(x)) for x in range(1, 6)])
    assign = SelectField("Choose Computer", choices=[("Personal", "Personal")] +
                                                    [(str(x), str(x)) for x in range(1, 35)])
    submit = SubmitField("Submit")
