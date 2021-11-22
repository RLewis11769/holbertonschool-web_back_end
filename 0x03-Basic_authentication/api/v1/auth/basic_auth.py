#!/usr/bin/env python3
""" Class to manage Basic API authentication """
from api.v1.auth.auth import Auth
from base64 import b64decode
from typing import Tuple


class BasicAuth(Auth):
    """ Basic Auth class """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """
        Returns Base64 part of Authorization header

        Args:
            authorization_header: Encoded authorization header
        """
        # Note: authorization header starts with "Basic "
        if authorization_header is not None:
            if type(authorization_header) is str:
                if authorization_header.startswith("Basic "):
                    return (authorization_header[6:])
        return (None)

    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                           str) -> str:
        """
        Returns decoded authorization header

        Args:
            base64_authorization_header: Base64 encoded authorization header
        """
        try:
            # Decode base64 bytes to utf-8 string
            return b64decode(base64_authorization_header).decode("utf-8")
        except Exception:
            # Exceptions include not string and None
            return(None)

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header:
                                 str) -> Tuple[str, str]:
        """
        Returns user email and password from authorization header

        Args:
            decoded_base64_authorization_header: Decoded authorization header
        """
        # Edge cases that return (None, None) failure message
        if decoded_base64_authorization_header is None or \
        type(decoded_base64_authorization_header) is not str or \
        ":" not in decoded_base64_authorization_header:
            return(None, None)
        else:
            # Note: authorization header is in the form "email:password"
            # Split auth header into email and password values on :
            # Cast returned list as tuple
            return(tuple(decoded_base64_authorization_header.split(":")))
