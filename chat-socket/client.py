# Equipe: Rodrigo Miranda, Clovis Chakrian, Ana Cecilia

import socket

HEADER = 64
PORT = 5050
FORMAT = 'UTF-8'
DISCONNECT_MESSAGE = "sair"
SERVER = "10.1.13.161"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

while True:
    user_input = input("Enter your message (Escreva sair para sair!): ")
    
    if user_input == DISCONNECT_MESSAGE:
        send(DISCONNECT_MESSAGE)
        break
    
    send(user_input)

client.close()
