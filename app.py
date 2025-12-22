# run me with 'flask --app app run'

from flask import Flask, render_template, jsonify
import sqlite3
from pathlib import Path

app = Flask(__name__)
application = app
# DB_PATH = Path("counter.db")

@app.route("/")
def hello_world():
    return render_template('index.html') #, person=name)