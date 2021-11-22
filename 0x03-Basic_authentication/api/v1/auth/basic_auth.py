#!/usr/bin/env python3
""" Class to manage Basic API authentication """
from api.v1.auth.auth import Auth
from base64 import b64decode
from flask import request
from typing import List, TypeVar


class BasicAuth(Auth):
    """ Basic Auth class """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ Returns Base64 part of Authorization header """
        # Note: authorization header starts with "Basic "
        if authorization_header is not None:
            if type(authorization_header) is str:
                if authorization_header.startswith("Basic "):
                    return (authorization_header[6:])
        return (None)

    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                           str) -> str:
        """ Decode encoded authorization header """
        # if base64_authorization_header is None:
        #     if type(base64_authorization_header) is not str:
        #         return(None)
        try:
            # Decode base64 bytes to utf-8 string
            return b64decode(base64_authorization_header).decode("utf-8")
        except Exception:
            return(None)
