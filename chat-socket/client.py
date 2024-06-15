# Equipe: Rodrigo Miranda, Clovis Chakrian, Ana Cecilia

import socket
import threading

HEADER = 64
PORT = 5050
FORMAT = 'UTF-8'
DISCONNECT_MESSAGE = "sair"
#SERVER = "10.1.13.161"
SERVER = socket.gethostbyname(socket.gethostbyname())
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def handle_client():
    print(client.recv(2048).decode(FORMAT))

def send():
    msg = input()
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

while True:
    threadMsg = threading.Thread(target=send)
    threadMsg.start()
    thread = threading.Thread(target=handle_client)
    thread.start()
    