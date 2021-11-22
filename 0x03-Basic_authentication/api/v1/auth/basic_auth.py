#!/usr/bin/env python3
""" Class to manage Basic API authentication """
from api.v1.auth.auth import Auth
from flask import request
from typing import List, TypeVar


class BasicAuth(Auth):
    """ Basic Auth class """
    pass
