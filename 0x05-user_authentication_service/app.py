#!/usr/bin/env python3
""" Authorization module """
from auth import Auth
from flask import Flask, jsonify, request


AUTH = Auth()
app = Flask(__name__)


@app.route("/", methods=['GET'])
def index():
    """ Index route """
    return jsonify({'message': 'Bienvenue'})


@app.route("/users", methods=['POST'])
def register():
    """ Register route """
    email = request.form.get('email')
    pw = request.form.get('password')
    try:
        AUTH.register_user(email=email, password=pw)
        return jsonify({'email': email, 'message': 'user created'})
    except ValueError:
        return (jsonify({'message': 'email already registered'}), 400)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
