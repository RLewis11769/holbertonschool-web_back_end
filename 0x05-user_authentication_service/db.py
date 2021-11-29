#!/usr/bin/env python3
""" DB module """
from sqlalchemy import create_engine
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.session import Session
from user import Base, User


class DB:
    """ DB class """

    def __init__(self) -> None:
        """ Initialize a new DB instance """
        self._engine = create_engine("sqlite:///a.db")
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """ Memoized session object """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """
        Add new user to database and returns object

        Args:
            email: user's email
            hashed_password: hashed password
        """
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return (user)

    def find_user_by(self, **kwargs: dict) -> User:
        """
        Finds user by given args and return first row as filtered by input

        Args:
            kwargs: dict of args to filter by
        """
        try:
            return self._session.query(User).filter_by(**kwargs).one()
        except NoResultFound:
            raise NoResultFound
        except InvalidRequestError:
            raise InvalidRequestError

    def update_user(self, user_id: int, **kwargs: dict) -> User:
        """
        Updates given user by given args and returns updated object

        Args:
            user_id: user's id
            kwargs: dict of args to update by
        """
        user = self.find_user_by(id=user_id)
        try:
            for key, value in kwargs.items():
                setattr(user, key, value)
            self._session.commit()
            return (user)
        except ValueError:
            raise ValueError
