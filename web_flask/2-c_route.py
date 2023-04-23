#!/usr/bin/python3
"""Starts a Flask web application.
The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """This function displays Hello HBNB!"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """This function displays HBNB"""
    return "HBNB"



@app.route("/hbnb", strict_slashes=False)
def c(text):
    """display “C ” followed by the value of the text variable (replace underscore _ symbols with a space"""
    text = text.replace("_"," ")
    return "c %s" %text


if __name__ == "__main__":
    app.run(host="0.0.0.0")
