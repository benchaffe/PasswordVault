import os.path

from cryptography.fernet import Fernet

import key

if os.path.isfile('key.key'):
    key = key.load_key()
else:
    key.write_key()
    key = key.load_key()


def encrypt(password: str) -> bytes:
    """
    Encrypts the password and returns the result
    :param password: (Str) Password you want encrypting
    :return: The encrypted password
    """
    f = Fernet(key)
    password = password.encode()
    encrypted = f.encrypt(password)
    return encrypted


def decrypt(encrypted_pass: bytes) -> bytes:
    """
    Decrypts the given password
    :rtype: str
    :param encrypted_pass: The encrypted password to decrypt
    :return: The original password
    """
    f = Fernet(key)
    password: bytes = f.decrypt(encrypted_pass)
    return password
