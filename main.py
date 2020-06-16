import os.path

import database
import encryption as e

if not os.path.isfile('vault.db'):
    database.create_database()


def run_vault():
    """
    Runs the program
    :return:
    """
    response = input("Type 1 to add credentials to the vault \nType 2 to view your vault \nType 3 to retrieve a "
                     "password \n")
    response = str(response)

    while response != "1" and response != "2" and response != "3":
        print("That is not a valid function, try again")
        response = input("Type 1 to add credentials to the vault \nType 2 to view your vault \nType 3 to retrieve a "
                         "password \n")

    if response == "1":
        website = input("Please enter the website you would like to store your credentials for:")
        email = input("Please enter the email you use to login")
        password = input("Please enter the password you use to login")

        encrypted = e.encrypt(password)

        database.update(website, email, encrypted)
    elif response == "2":
        database.view_db()
    elif response == "3":
        database.view_db()
        website_id = input("Please input the ID you would like your credentials for as a number:\n")
        credentials = database.get_credentials(website_id)
        print("Your credentials for " + credentials[0] + ":\nEmail: " + credentials[1] + "\nPassword: " + credentials[2])
    return 0


if __name__ == "__main__":
    run_vault()
