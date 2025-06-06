import sys
from typing import Dict
import json


def app_startup():
    print('Welcome to the game streaming app!')

    while True:
        option = input('Enter 1 to login or enter 2 to exit: ')

        if option == '1':
            username = input("\nEnter username: ")
            password = input("Enter password: ")
            if username == "user" and password == "password":
                print("Login successful!")
                main_menu()
            else:
                print("Login failed.")
        elif option == '2':
            print("\nThank you for using this application!")
            sys.exit(0)
        else:
            print("Invalid choice. Please try again!")

def main_menu():
    while True:
        print("\nMenu: ")
        print("1. Start game")
        print("2. Logout")
        option = input("Select an option: ")

        if option == '1':
            game_stream()
        elif option == '2':
            print("You are logging out.\n")
            app_startup()
        else:
            print("Invalid choice. Please try again!")


def game_stream():
    print("In game!")
    sys.exit(0)


if __name__ == "__main__":
    app_startup()
