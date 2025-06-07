import sys
import asyncio
from aioquic.quic.configuration import QuicConfiguration
from aioquic.asyncio import connect
from aioquic.asyncio.protocol import QuicConnectionProtocol
from quic_stream import EchoQuicConnection, QuicStreamEvent
import pdu


async def app_startup(conn:EchoQuicConnection):
    print('Welcome to the game streaming app!')

    # Sign in menu
    while True:
        option = input('Enter 1 to login or enter 2 to exit: ')

        if option == '1':
            username = input("\nEnter username: ")
            password = input("Enter password: ")
            if username == "user" and password == "password":
                print("Login successful!")
                await main_menu(conn)
            else:
                print("Login failed.")
        elif option == '2':
            print("\nThank you for using this application!")
            sys.exit(0)
        else:
            print("Invalid choice. Please try again!")

async def main_menu(conn:EchoQuicConnection):
    # Main menu to select game
    while True:
        print("\nMenu: ")
        print("1. Start game")
        print("2. Logout")
        option = input("Select an option: ")

        if option == '1':
            await game_stream_client(conn)
        elif option == '2':
            print("You are logging out.\n")
            await app_startup(conn)
        else:
            print("Invalid choice. Please try again!")


async def game_stream_client(conn:EchoQuicConnection):
    print("[cli] Starting game")
    print("[cli] Begin entering inputs: ")

    while True:
        data = input("[cli] Enter an input: ")[0]
        datagram = pdu.Datagram(pdu.VERSION_NUM, data, 1, 1, 1)

        new_stream_id = conn.new_stream()

        qs = QuicStreamEvent(new_stream_id, datagram.to_bytes(), False)
        await conn.send(qs)
        msg:QuicStreamEvent = await conn.receive()
        dgram_resp = pdu.Datagram.from_bytes(msg.data)

        print(f"[cli] Server received '{dgram_resp.data}' input")