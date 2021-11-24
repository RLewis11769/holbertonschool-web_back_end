#!/usr/bin/env python3
""" Module of Users views """
from werkzeug.wrappers import response
from api.v1.views import app_views
from api.v1.auth.session_auth import SessionAuth
from flask import abort, jsonify, request, make_response
from models.user import User
from os import getenv


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """ kdj """
    email = request.form.get('email')
    if email is None:
        return (jsonify({"error": "email missing"}), 400)
    pw = request.form.get('password')
    if pw is None:
        return (jsonify({"error": "password missing"}), 400)
    search = User.search({'email': email})
    if len(search) == 0:
        return (jsonify({"error": "no user found for this email"}), 401)
    for user in search:
        if not user.is_valid_password(pw):
            return (jsonify({"error": "wrong password"}), 401)
        else:
            from api.v1.app import auth
            session_id = auth.create_session(user.id)
            user_id = auth.user_id_for_session_id(session_id)
            # Find user instance based on user id
            user_obj = User.get(user_id)
            # Create a response object by jsonifying the user object
            response = jsonify(user_obj.to_json())
            # Set cookie to session id
            response.set_cookie(getenv('SESSION_NAME'), session_id)
            return (response)
