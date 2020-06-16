import sqlite3

import encryption as e


def update(website: str, email: str, encrypted_pass: bytes) -> None:
    """
    Connects to the database
    :rtype: None
    :param website: (Str) Web address of saved login details
    :param email: (Str) Email address used to login
    :param encrypted_pass: (bytes) Encrypted password used to login
    :return:
    """
    conn = sqlite3.connect('vault.db')
    c = conn.cursor()
    sql = '''INSERT INTO PASSWORDS (website, email, encrypted) VALUES (?, ?, ?)'''
    items = [website, email, encrypted_pass]
    c.execute(sql, items)
    conn.commit()


def create_database() -> None:
    """
    Creates a database to store the passwords in
    :return:
    """
    conn = sqlite3.connect('vault.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE PASSWORDS ([website_id] INTEGER PRIMARY KEY, [website] text, [email] text, 
    [encrypted] text)''')
    conn.commit()


def view_db() -> None:
    """
    Prints the whole database
    :return:
    """
    conn = sqlite3.connect('vault.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM PASSWORDS''')
    rows = c.fetchall()
    for row in rows:
        print(row)


def get_credentials(website_id):
    """
    Gets the row for the selected website
    :rtype: list
    :param: The id you would like the credentials for
    :return: Returns the list of credentials
    """
    conn = sqlite3.connect('vault.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM PASSWORDS WHERE website_id=?''', website_id)
    row = c.fetchall()
    website = str(row[0][1])
    email = str(row[0][2])
    encrypted = row[0][3]
    password = str(e.decrypt(encrypted))
    return [website, email, password]
