#!/usr/bin/env python3

from flask import Flask, jsonify, request

app = Flask(__name__)


# In-memory user dictionary
users = {}


@app.route("/", methods=["GET"])
def home():
    """
    Root endpoint that returns a welcome message.
    """
    return "Welcome to the Flask API!"


@app.route("/status", methods=["GET"])
def status():
    """
    Endpoint to check the status of the API.
    Returns 'OK' as a plain text response.
    """
    return "OK"


@app.route("/data", methods=["GET"])
def get_usernames():
    """
    Returns a JSON list of all usernames stored in the API.
    """
    return jsonify(list(users.keys()))


@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    """
    Returns the full user object for the given username.
    If the user is not found, returns a 404 error.
    """
    if username in users:
        return jsonify(users[username])
    return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """
    Adds a new user to the users dictionary.
    Expects a JSON object with 'username', 'name', 'age', and 'city'.
    Returns a confirmation message with the added user's data.
    If 'username' is not provided, returns a 400 error.
    If 'username' already exists, returns a 400 error with an appropriate message.
    """
    data = request.get_json()
    if not data or "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data["username"]
    if username in users:
        return jsonify({
            "error": "User already exists",
            "user": users[username]
        }), 400

    users[username] = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }

    return jsonify({
        "message": "User added",
        "user": users[username]
    }), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

