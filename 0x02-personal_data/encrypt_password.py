#!/usr/bin/env python3
""" File containing functions to hash password and verify """
import bcrypt


def hash_password(password: str) -> bytes:
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


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Validate that provided password matches hashed password

    Args:
        hashed_password: hashed password to be compared/verified
        password: password to be compared/verified
    Returns True if password is valid, False otherwise
    """
    pw = password.encode('utf-8')
    return (bcrypt.checkpw(pw, hashed_password))
