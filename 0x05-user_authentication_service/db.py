#!/usr/bin/env python3
""" DB module """
from sqlalchemy import create_engine
from sqlalchemy.exc import InvalidRequestError
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

    def find_user_by(self, **kwargs) -> User:
        """
        Finds user by given args and returns first row as filtered by kwargs

        Args:
            kwargs: dict of args to filter by
        """
        try:
            return self._session.query(User).filter_by(**kwargs).one()
        except NoResultFound:
            raise NoResultFound
        except InvalidRequestError:
            raise InvalidRequestError

    def update_user(self, user_id: int, **kwargs) -> None:
        """
        Updates given user by given args, no return

        Args:
            user_id: user's id
            kwargs: dict of args to update by
        """
        try:
            user = self.find_user_by(id=user_id)
            for key, value in kwargs.items():
                if hasattr(user, key):
                    setattr(user, key, value)
                else:
                    raise ValueError
            self._session.commit()
        except Exception:
            raise ValueError
