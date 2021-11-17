#!/usr/bin/env python3
""" File containing functions to hash password and verify """
import bcrypt


def hash_password(password: str) -> str:
    """
    Return salted, hashed password as byte string

    Args:
        password: password to be hashed
    Returns hashed password as byte string
    """
    pw = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(pw, salt)
    return (hashed_password)
