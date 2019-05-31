from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
#import select

def receive():
    """Handles receiving of messages."""
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode("utf8")
            print(f'{msg}')
        except OSError:  # Possibly client has left the chat.
            break

HOST = "127.0.0.1"
PORT = 1234

BUFSIZ = 1024
ADDR = (HOST, PORT)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

receive_thread = Thread(target=receive)
receive_thread.start()

while True:
    message = input()

    if message:
        if message == "/quit":
            message = message.encode('utf-8')
            client_socket.send(message)
            client_socket.close()
            break
        else:    
            message = message.encode('utf-8')
            client_socket.send(message)