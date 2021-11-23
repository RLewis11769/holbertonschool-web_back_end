#!/usr/bin/env python3
""" Route module for the API """
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
from os import getenv


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})


auth = None
auth_type = getenv("AUTH_TYPE")
if auth_type == "auth":
    # Assign correct instance of authentication
    from api.v1.auth.auth import Auth
    auth = Auth()
if auth_type == "basic_auth":
    # Assign correct instance of authentication
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()


@app.errorhandler(401)
def not_authorized(error) -> str:
    """ Handler to return response when 401 not authorized error raised """
    return (jsonify({"error": "Unauthorized"}), 401)


@app.errorhandler(403)
def forbidden(error) -> str:
    """ Handler to return response when user doesn't have access - code 403 """
    return (jsonify({"error": "Forbidden"}), 403)


@app.errorhandler(404)
def not_found(error) -> str:
    """ Handler to return response when 404 not found error raised """
    return (jsonify({"error": "Not found"}), 404)


@app.before_request
def before_request():
    """ Filter requests to proper error handlers if necessary """
    # Create list of allowed endpoints
    auth_list = ["/api/v1/status/",
                 "/api/v1/unauthorized",
                 "/api/v1/forbidden"]

    # Make sure auth has valid endpoint
    if auth and auth.require_auth(request.path, auth_list):
        if auth.authorization_header(request) is None:
            # No proper authorization header raises unauthorized
            abort(401)
        if auth.current_user(request) is None:
            # Not a current user raises forbidden
            abort(403)
        else:
            request.current_user = auth.current_user(request)


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port, debug=True)
