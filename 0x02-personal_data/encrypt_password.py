#!/usr/bin/env python3
""" File containing functions to hash password and verify """
import bcrypt


def hash_password(password: str) -> bytes:
    """
    Returns salted, hashed password as byte string

    Args:
        password: password to be hashed
    """
    # Encode password to bytes
    pw = password.encode('utf-8')
    # Salt is fixed-length random value added to input
    # Makes sure unique hash for each input
    salt = bcrypt.gensalt()
    # Return hashed password with salt
    return (bcrypt.hashpw(pw, salt))


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Returns T/F validatation that provided password matches hashed password

    Args:
        hashed_password: hashed password to be compared/verified
        password: password to be compared/verified
    Returns True if password is valid, False otherwise
    """
    # Encode password to bytes
    pw = password.encode('utf-8')
    # Use built-in checkpw function to compare hashed password
    return (bcrypt.checkpw(password, hashed_password))
