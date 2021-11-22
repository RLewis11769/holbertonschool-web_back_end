#!/usr/bin/env python3
""" Class to manage Basic API authentication """
from api.v1.auth.auth import Auth
from flask import request
from typing import List, TypeVar


class BasicAuth(Auth):
    """ Basic Auth class """

    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """ Returns Base64 part of Authorization header """
        # Note: authorization header starts with "Basic "
        if authorization_header is not None and type(authorization_header) is str:
            if authorization_header.startswith("Basic "):
                return (authorization_header[6:])
        return (None)
