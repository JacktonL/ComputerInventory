from app.routes import app
from flask import request, render_template
from .Classes import Comment
from .Forms import CommentForm
from datetime import datetime
from flask import session, flash


@app.route("/comments", methods=["POST", "GET"])
def comments():

    date = datetime.now()
    hour = date.strftime("%I")
    sum = int(hour) + 4
    if sum > 12:
        sum -= 12
    date_string = date.strftime("{}:%M %m/%d/%y".format(str(sum)))
    form = CommentForm(request.form)

    if request.method == "POST" and form.validate():

        if session.get("displayName"):

            name = session.get("displayName")
            comment = form.comment.data

            commentObj = Comment()

            commentObj.full_name = name
            commentObj.date = date_string
            commentObj.comment = comment

            commentObj.save()

        else:

            flash("Login to Comment")

    return render_template("comments.html", form=form, objs=list(Comment.objects)[::-1])
