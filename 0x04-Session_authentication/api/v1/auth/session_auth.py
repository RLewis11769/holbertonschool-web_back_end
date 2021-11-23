#!/usr/bin/env python3
""" Class to manage Session authentication """
from api.v1.auth.auth import Auth
from uuid import uuid4


class SessionAuth(Auth):
    """ Session Auth class """

    # Class attribute to hold relationship between session id and user id
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        Returns created session id for given user id
        Adds session id as key of dict with user id as value

        Args:
            user_id: given user id to create session id for, used as value
        """
        if user_id is None or type(user_id) is not str:
            return (None)
        session_id = str(uuid4())
        self.user_id_by_session_id.update({session_id: user_id})
        return (session_id)

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        Return user id based on session id

        Args:
            session_id: session id to get user id for
        """
        if session_id is None or type(session_id) is not str:
            return (None)
        return (self.user_id_by_session_id.get(session_id))
