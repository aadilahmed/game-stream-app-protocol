import sys
from typing import Dict
from quic_stream import EchoQuicConnection, QuicStreamEvent
import json
import pdu


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


async def game_stream(conn:EchoQuicConnection):
    print("[cli] Starting game")
    print("[cli] Begin entering inputs: ")

    


if __name__ == "__main__":
    app_startup()