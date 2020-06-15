import os.path
import database
import encrypt as e

if not os.path.isfile('vault.db'):
    database.create_database()

website = input("Please enter the website you would like to store your credentials for:")
email = input("Please enter the email you use to login")
password = input("Please enter the password you use to login")

encrypted = e.encrypt(password)

database.update(website, email, encrypted)
