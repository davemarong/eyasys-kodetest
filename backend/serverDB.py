from __future__ import print_function  # In python 2.7
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
import sys

app = Flask(__name__)

# the name of the database; add path if necessary
db_name = "newdb.db"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + db_name

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

# this variable, db, will be used for all SQLAlchemy commands
db = SQLAlchemy(app)


class Sock(db.Model):
    __tablename__ = "socks"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    style = db.Column(db.String)
    color = db.Column(db.String)


def reCreateDB():
    db.drop_all()
    db.create_all()


@app.route("/")
def testdb():
    try:
        db.session.query(text("1")).from_statement(text("SELECT 1")).all()
        return "<h1>It works.</h1>"
    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = "<h1>Something is broken.</h1>"
        return hed + error_text


@app.route("/readData")
def index():
    try:
        socks = Sock.query.all()
        sock_text = "<ul>"
        for sock in socks:
            sock_text += "<li>" + sock.name + ", " + sock.color + "</li>"
        sock_text += "</ul>"
        print(socks, file=sys.stderr)
        return sock_text
    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = "<h1>Something is broken.</h1>"
        return hed + error_text


@app.route("/phones")
def get_phones():
    return [
        {"Phone": "46807041", "Merke": "Apple", "Modell": "13"},
        {"Phone": "46807041", "Merke": "Apple", "Modell": "14"},
        {"Phone": "46807041", "Merke": "Apple", "Modell": "15"},
        {"Phone": "46807041", "Merke": "Apple", "Modell": "16"},
    ]


@app.route("/postData", methods=["POST", "GET"], strict_slashes=False)
def get_time():

    # Returning an api for showing in  reactjs
    return {"name": "geek", "description": "22"}
