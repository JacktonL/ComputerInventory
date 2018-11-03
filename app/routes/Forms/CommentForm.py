from flask_wtf import FlaskForm
from wtforms import *


class CommentForm(FlaskForm):

    first_name = StringField()
    last_name = StringField()
    comment = TextAreaField()
    submit = SubmitField()
