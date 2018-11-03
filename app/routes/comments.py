from app.routes import app
from flask import request, render_template
from .Classes import Comment
from .Forms import CommentForm
from datetime import datetime


@app.route("/comments", methods=["POST", "GET"])
def comments():

    form = CommentForm(request.form)

    if request.method == "POST" and form.validate():

        first = form.first_name.data
        last = form.last_name.data
        comment = form.comment.data

        commentObj = Comment()

        commentObj.first_name = first
        commentObj.last_name = last
        commentObj.date = datetime.now()
        commentObj.comment = comment

        commentObj.save()

    return render_template("comments.html", form=form, objs=Comment.objects)