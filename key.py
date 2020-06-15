from cryptography.fernet import Fernet

def write_key():
    """
    Generates a key and saves it to a file
    :return:
    """
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    """
    Loads the key from the current directory
    :return:
    """
    return open("key.key", "rb").read()

