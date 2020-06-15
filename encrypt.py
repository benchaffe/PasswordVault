from cryptography.fernet import Fernet
import key
import os.path

if os.path.isfile('key.key'):
    key = key.load_key()
else:
    key.write_key()
    key = key.load_key()


def encrypt(password):
    """
    Encrypts the password and returns the result
    :param password: (Str) Password you want encrypting
    :return: The encrypted password
    """
    f = Fernet(key)
    password = password.encode()
    encrypted = f.encrypt(password)
    return encrypted
