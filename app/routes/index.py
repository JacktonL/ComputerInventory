
import requests
from app.routes import app
from flask import render_template, session, redirect, request
from requests_oauth2.services import GoogleClient
from requests_oauth2 import OAuth2BearerToken


google_auth = GoogleClient(
    client_id=("624093337065-fqd6k7v5sqgj1l10kit6dhd6qofq8jat"
               ".apps.googleusercontent.com"),
    client_secret="9UEX16NlzET-aPgdntBy7Bfi",
    redirect_uri="http://localhost:5000/oauth2callback"
)


@app.route('/')
def index():
    return render_template("index.html", name=session.get("displayName"))


@app.route('/login')
def login():
    if not session.get("access_token"):
        return redirect("/oauth2callback")
    with requests.Session() as s:
        s.auth = OAuth2BearerToken(session["access_token"])
        r = s.get("https://www.googleapis.com/plus/v1/people/me?access_token={}".format(session.get("access_token")))
    r.raise_for_status()
    data = r.json()
    return render_template("index.html", name=data["displayName"])


@app.route("/oauth2callback")
def google_oauth2callback():
    code = request.args.get("code")
    error = request.args.get("error")
    if error:
        return "error :( {!r}".format(error)
    if not code:
        return redirect(google_auth.authorize_url(
            scope=["profile", "email"],
            response_type="code",
        ))
    data = google_auth.get_token(
        code=code,
        grant_type="authorization_code",
    )
    session["access_token"] = data.get("access_token")
    return redirect("/login")
