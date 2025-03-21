#!/usr/bin/env python3

from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory users storage
users = {}

@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/data")
def data():
    # Return a list of all usernames stored in the API
    return jsonify(list(users.keys()))

@app.route("/status")
def status():
    return "OK"

@app.route("/users/<username>")
def get_user(username):
    # Return the full object corresponding to the provided username
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=["POST"])
def add_user():
    # Parse the incoming JSON data
    user_data = request.get_json()

    # Check if username is provided
    if "username" not in user_data:
        return jsonify({"error": "Username is required"}), 400

    # Extract username
    username = user_data["username"]

    # Add the new user to the users dictionary
    users[username] = user_data

    # Return a confirmation message with the added user's data
    return jsonify({
        "message": "User added",
        "user": user_data
    }), 201

if __name__ == "__main__":
    app.run(debug=True)
