#!/usr/bin/env python3

from flask import Flask
from flask import jsonify
from flask import request


app = Flask(__name__)
users = {}

@app.route("/")
def home():
    return ("Welcome to the Flask API!")

@app.route("/data")
def json():
    return jsonify(list(users.keys()))

@app.route("/status")
def status():
    return ("OK")

@app.route("/users/<username>")
def get_user(username):
    user = users.get(username)

    if user:
        return jsonify(user)
    else:
        return jsonify("error":"User not found"), 404

if __name__ == "__main__":
    app.run()

