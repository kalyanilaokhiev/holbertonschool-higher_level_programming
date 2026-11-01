#!/usr/bin/env python3

from flask import Flask
from flask import jsonify
from flask import request


app = Flask(__name__)
users = {}


@app.route("/")
def home():
    """Define a route for the root URL ("/") """
    return ("Welcome to the Flask API!")


@app.route("/data")
def json():
    """Create a new route /data and associate a function with it."""
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    """Checking status"""
    return ("OK")


@app.route("/users/<username>")
def get_user(username):
    """Returns the full object corresponding to the provided"""
    user = users.get(username)

    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """Create a new route /add_user that accepts POST requests."""
    # parsing data
    user = request.get_json(silent=True)

    # if the request body is not valid JSON
    if user is None:
        return jsonify({"error": "Invalid JSON"}), 400

    # get username
    username = user.get("username")

    # If username is missing
    if not username:
        return jsonify({"error": "Username is required"}), 400

    # If user exist
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # add user
    users[username] = user

    # confirmation message with the added user's data
    return jsonify({
        "message": "User added",
        "user": user
    }), 201


if __name__ == "__main__":
    app.run()
