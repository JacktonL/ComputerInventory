from flask_wtf import FlaskForm
from wtforms import *


class CommentForm(FlaskForm):

    comment = TextAreaField()
    submit = SubmitField()
