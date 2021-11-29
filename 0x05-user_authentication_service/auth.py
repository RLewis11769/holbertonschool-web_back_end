#!/usr/bin/env python3
""" Authorization module """
from bcrypt import hashpw, gensalt
from db import DB
from sqlalchemy.orm.exc import NoResultFound
from user import User


class Auth:
    """ Auth class to interact with the authentication database """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        Registers new user in the database and returns object if new user

        Args:
            email: user's email
            password: user's password
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError("User {} already exists".format(email))
        except NoResultFound:
            pw = _hash_password(password)
            user = self._db.add_user(email, pw)
            return (user)


def _hash_password(password: str) -> bytes:
    """
    Returns hashed and salted password

    Args:
        password: password to hash
    """
    pw = password.encode('utf-8')
    return (hashpw(pw, gensalt()))
