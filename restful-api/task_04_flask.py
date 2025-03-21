#!/usr/bin/env python3

from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory user dictionary
users = {}

@app.route("/", methods=["GET"])
def home():
    """Root endpoint that returns a welcome message."""
    return "Welcome to the Flask API!"

@app.route("/status", methods=["GET"])
def status():
    """Endpoint to check the status of the API."""
    return "OK"

@app.route("/data", methods=["GET"])
def get_usernames():
    """Returns a JSON list of all usernames stored in the API."""
    return jsonify(list(users.keys()))

@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    """Returns the full user object for the given username."""
    if username in users:
        return jsonify(users[username])
    return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=["POST"])
def add_user():
    """Adds a new user to the users dictionary."""
    data = request.get_json()
    if not data or "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data["username"]
    if username in users:
        return jsonify({"error": "User already exists"}), 400

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

