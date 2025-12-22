# run me with 'flask --app app run'

from flask import Flask, render_template, jsonify
import sqlite3
from pathlib import Path
from flask_sqlalchemy import SQLAlchemy
import os
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import update
from flask import redirect, url_for

app = Flask(__name__)
application = app

# DB
app.config['SECRET_KEY'] = "ducksareverysecretive1234"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///ducks.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Counter(db.Model):
    __tablename__ = "counter"
    name = db.Column(db.String, primary_key=True, default="main")
    value = db.Column(db.Integer, nullable=False, default=0)

with app.app_context():
    if not os.path.exists("ducks.db"):
        db.create_all()

# SITE
@app.route("/")
def hello_world():
    duck_likes = db.session.get(Counter, "main")
    if duck_likes is not None:
        value = duck_likes.value
        return render_template("index.html", counter=value)
    else:
        return render_template("index.html", counter=99)
        # CREATE????

@app.post("/increment")
def increment():
    db.session.execute(
        update(Counter)
        .where(Counter.name == "main")
        .values(value=Counter.value + 1)
    )
    db.session.commit()
    duck_likes = db.session.get(Counter, "main").value
    return jsonify(value=duck_likes)