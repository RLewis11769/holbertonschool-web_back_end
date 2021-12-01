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
        except Exception:
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

    def get_user_from_session_id(self, session_id: str) -> User:
        """
        Return user object corresponding to session ID

        Args:
            session_id: session ID to find user for
        """
        try:
            user = self._db.find_user_by(session_id=session_id)
            return (user)
        except Exception:
            return (None)

    def destroy_session(self, user_id: int) -> None:
        """
        Destroy/delete session for user with given ID

        Args:
            user_id: ID of user to destroy session for
        """
        try:
            user = self._db.find_user_by(id=user_id)
            self._db.update_user(user.id, session_id=None)
        except Exception:
            return (None)

    def get_reset_password_token(self, email: str) -> str:
        """
        Return newly-created reset password token
        Find user corresponding to given email, generate new uuid as
            reset_token, store in database, and return new token

        Args:
            email: email of user to create reset token for
        """
        try:
            user = self._db.find_user_by(email=email)
            reset_token = _generate_uuid()
            self._db.update_user(user.id, reset_token=reset_token)
            return (reset_token)
        except Exception:
            raise ValueError

    def update_password(self, reset_token: str, password: str) -> None:
        """
        Update user's password with given password using reset token

        Args:
            reset_token: reset token for user (identifying user)
            password: user's new password
        """
        try:
            user = self._db.find_user_by(reset_token=reset_token)
            pw = _hash_password(password)
            self._db.update_user(user.id, hashed_password=pw, reset_token=None)
        except Exception:
            raise ValueError


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
