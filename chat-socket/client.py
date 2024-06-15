# Equipe: Rodrigo Miranda, Clovis Chakrian, Ana Cecilia
import ctypes
libgcc_s = ctypes.CDLL('libgcc_s.so.1')
import socket
import threading

HEADER = 64
PORT = 5050
FORMAT = 'UTF-8'
DISCONNECT_MESSAGE = "sair"
SERVER = "192.168.67.135"
#SERVER = socket.gethostbyname(socket.gethostname())

ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def handle_client():
    while True:
        try:
            message = client.recv(2048).decode(FORMAT)
            if message:
                print(message)
            else:
                print("Desconectado do servidor.")
                break
        except:
            print("Erro na conexão com o servidor.")
            break

def send():
    while True:
        msg = input('Digite sua mensagem: ')
        if msg == DISCONNECT_MESSAGE:
            send_message(DISCONNECT_MESSAGE)
            break
        
        if msg != '':
            send_message(msg)

def send_message(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

thread_recv = threading.Thread(target=handle_client)
thread_recv.start()

thread_send = threading.Thread(target=send)
thread_send.start()

thread_recv.join()
thread_send.join()

client.close()