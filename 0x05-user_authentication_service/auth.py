#!/usr/bin/env python3
""" Authorization module """
from bcrypt import checkpw, hashpw, gensalt
from db import DB
from sqlalchemy.orm.exc import NoResultFound
from user import User
from uuid import uuid4


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

    def valid_login(self, email: str, password: str) -> bool:
        """
        Returns true if able to locate email and password matches

        Args:
            email: user's email
            password: user's password
        """
        try:
            user = self._db.find_user_by(email=email)
            pw = password.encode('utf-8')
            return checkpw(pw, user.hashed_password)
        except NoResultFound:
            return (False)

    def create_session(self, email: str) -> str:
        """
        Return newly-created session ID
        Find user corresponding to given email, generate new uuid as
            session_id, store in database, and return new session_id

        Args:
            email: email of user to create session for
        """
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return (session_id)
        except Exception:
            return (None)


def _hash_password(password: str) -> bytes:
    """
    Returns hashed and salted password

    Args:
        password: password to hash
    """
    pw = password.encode('utf-8')
    return (hashpw(pw, gensalt()))


def _generate_uuid() -> str:
    """ Returns string representation of new random uuid """
    return (str(uuid4()))
