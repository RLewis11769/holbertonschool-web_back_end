#!/usr/bin/env python3
""" Class to manage API authentication """
from flask import request
from os import getenv
from typing import List, TypeVar


class Auth():
    """ Template for other authentication systems """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Returns true if path not in list of excluded paths

        Args:
            path: path to check
            excluded_paths: list of paths to exclude
        """
        if path is None or excluded_paths is None:
            return (True)
        # Loop through list to check if path is in list
        if path in excluded_paths or f"{path}/" in excluded_paths:
            return(False)
        return (True)

    def authorization_header(self, request=None) -> str:
        """
        Returns Flask request object or None if no authorization header

        Args:
            request: Flask request object
        """
        # Make sure auth has endpoint - if not, return None so not error
        if request is None or request.headers.get('Authorization') is None:
            return (None)
        return (request.headers.get('Authorization'))

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Returns current user or None if no user

        Args:
            request: Flask request object
        """
        return (None)

    def session_cookie(self, request=None):
        """
        Returns cookie value from request

        Args:
            request: Flask request object
        """
        if request is None:
            return (None)
        cookie = getenv("SESSION_NAME")
        return (request.cookies.get(cookie))
