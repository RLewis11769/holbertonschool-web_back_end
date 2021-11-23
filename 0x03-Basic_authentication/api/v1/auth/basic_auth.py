#!/usr/bin/env python3
""" Class to manage Basic API authentication """
from api.v1.auth.auth import Auth
from base64 import b64decode
from models.base import DATA
from models.user import User
from typing import Tuple, TypeVar


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
            return (None)

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header:
                                 str) -> Tuple[str, str]:
        """
        Returns user email and password from authorization header

        Args:
            decoded_base64_authorization_header: Decoded authorization header
        """
        # Edge cases that return (None, None) failure message
        if (decoded_base64_authorization_header is None or
            type(decoded_base64_authorization_header) is not str or
           ":" not in decoded_base64_authorization_header):
            return (None, None)
        else:
            # Note: authorization header is in the form "email:password"
            # Split auth header into email and password values on :
            # Cast returned list as tuple
            return (tuple(decoded_base64_authorization_header.split(":")))

    def user_object_from_credentials(self, user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """
        Return user instance based on email and password

        Args:
            user_email: User email
            user_pwd: User password
        """
        if user_email is None or type(user_email) is not str:
            return (None)
        if user_pwd is None or type(user_pwd) is not str:
            return (None)
        try:
            # Search in base class - pass in dict, returns list
            search_list = User.search({'email': user_email})
            # Iterate through list to get string for use
            for user in search_list:
                # is_valid_pw in user class - pass in pwd, True is valid user
                if user.is_valid_password(user_pwd):
                    return (user)
        except Exception:
            return (None)

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Retrieves user instance object for request when given auth header

        Args:
            request: global request object default
        """
        auth = request.headers.get('Authorization')
        header = self.extract_base64_authorization_header(auth)
        decoded_h = self.decode_base64_authorization_header(header)
        email, pw = self.extract_user_credentials(decoded_h)
        return (self.user_object_from_credentials(email, pw))
