import sys
import hashlib
import re
import json
import os
from main_menu import main_menu
import load_save

JSON_USERS = "accounts.json"


class Account:
    def __init__(self, username, password):
        self.username = username
        #Storing the password to a hashed version
        self.password = password
        self.balance = 10000

    #username getter and setter
    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        if not value:
            raise ValueError("Username cannot be empty")
        self._username = value

    @property
    def password(self):
        return self._password_hash

    @password.setter
    def password(self, value):
        if not value:
            raise ValueError("Password cannot be empty")
        elif not self.validate_password(value):
            raise ValueError("Password has to be between 3 and 20 characters\n must have 1 uppercase, 1 number and 1 special symbol")
        self._password_hash = hashlib.sha256(value.encode()).hexdigest()

    #Validate the given password
    def validate_password(self, ps):
        if not 3 < len(ps) < 20:
            return False
        if not re.search(r"[A-Za-z]", ps):
            return False
        if not re.search(r"\d", ps):
            return False
        if not re.search(r"[!@#$%^&*()_+]", ps):
            return False
        return True
    #A method that returns new users data as a dict
    def to_dict(self):
        """Converting user data ato dict for easy JSON storage."""
        return {
            "username": self.username,
            "password_hash": self._password_hash,
            "balance": self.balance,
            "invested": {

            }
        }
#Register function returns True if successful
def register(username, password):
    new_acc = Account(username, password)
    new_acc_dict = new_acc.to_dict()

    accounts = load_save.load_users(JSON_USERS)

    for account in accounts:
        if account["username"] == new_acc_dict["username"]:
            print("\nUsername already exists\n")
            return False

    accounts.append(new_acc_dict)
    load_save.save_users(accounts, JSON_USERS)

    print("Registration successful")
    return True

#Login function returns True if successful
def login(username, password):
    accounts = load_save.load_users(JSON_USERS)

    if not accounts:
        print("Nobody is registered yet")
        return False

    pass_hash = hashlib.sha256(password.encode()).hexdigest()

    for account in accounts:
        if account["username"] == username and account["password_hash"] == pass_hash:
            print(f"\nLogin successful\n")
            return True


    print("Invalid username or password")
    return False


#Input Function returns users inputs as a tuple
def user_input():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    return (username, password)

def main():
    print("    WELCOME TO STOCK EXCHANGE APP\n")
    print("Please select one of the following options\n\n")
    print("\tType 1 to Login")
    print("\tType 2 to Register")
    print("\tType 3 to Exit\n\n")
    #User Chooses
    try:
        user_choice = int(input("Enter your choice: "))
        if user_choice not in [1, 2, 3]:
            sys.exit("Please provide one of the given choices")
    except ValueError:
        sys.exit("- please provide the given choices")

    #Login choice
    if user_choice == 1:
        username_login, password_login = user_input()
        if(login(username_login, password_login)):
            main_menu(username_login, True)

    #Register choice
    elif user_choice == 2:
        username, password = user_input()
        if(register(username, password)):
            main_menu(username, True)

    #Exit choice
    else:
        sys.exit("Goodbye!")

if __name__ == "__main__":
    main()
