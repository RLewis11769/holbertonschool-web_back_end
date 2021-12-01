#!/usr/bin/env python3
""" Authorization module """
from auth import Auth
from flask import abort, Flask, jsonify, request
from sqlalchemy.orm.exc import NoResultFound


AUTH = Auth()
app = Flask(__name__)


@app.route("/", methods=['GET'])
def index():
    """ Index route """
    return jsonify({'message': 'Bienvenue'})


@app.route("/users", methods=['POST'])
def register():
    """ Route to register new user """
    email = request.form.get('email')
    pw = request.form.get('password')
    try:
        AUTH.register_user(email=email, password=pw)
        return jsonify({'email': email, 'message': 'user created'})
    except ValueError:
        return (jsonify({'message': 'email already registered'}), 400)


@app.route("/sessions", methods=['POST'])
def login():
    """ Route to validate user credentials """
    email = request.form.get('email')
    pw = request.form.get('password')
    try:
        AUTH.valid_login(email=email, password=pw)
        session_id = AUTH.create_session(email=email)
        response = jsonify({'email': email, 'message': 'logged in'})
        response.set_cookie('session_id', session_id)
        return (response)
    except Exception:
        abort(401)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
