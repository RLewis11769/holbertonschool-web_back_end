from bcrypt import hashpw, gensalt

def _hash_password(password: str) -> bytes:
    """
    Returns hashed and salted password

    Args:
        password: password to hash
    """
    pw = password.encode('utf-8')
    salt = gensalt()
    return (hashpw(pw, salt))
