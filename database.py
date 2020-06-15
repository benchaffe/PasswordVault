import sqlite3


def update(website, email, encrypted_pass):
    """
    Connects to the database
    :param website: (Str) Web address of saved login details
    :param email: (Str) Email address used to login
    :param encrypted_pass: (Str) Encrypted password used to login
    :return:
    """
    conn = sqlite3.connect('vault.db')
    c = conn.cursor()
    sql = '''INSERT INTO PASSWORDS (website, email, encrypted) VALUES (?, ?, ?)'''
    items = [website, email, encrypted_pass]
    c.execute(sql, items)
    conn.commit()


def create_database():
    """
    Creates a database to store the passwords in
    :return:
    """
    conn = sqlite3.connect('vault.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE PASSWORDS ([website] text, [email] text, [encrypted] text)''')
    conn.commit()
