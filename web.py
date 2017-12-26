from flask import Flask
import dat
app = Flask(__name__)


@app.route("/")

def hello():
    return "Hello World!"

def get_data():
    usr = Flask.request_class.form['usr']
    dat.user_data(usr)