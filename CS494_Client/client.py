# Michael Long, Gennadii Sytov -- CS494 -- Client Application -- Server Class

# Imports / Constants
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
DEFAULT = 1080
BUFFER = 1024

# Designed to handle each of the server interactions for the client
class client_handler():

    # Init
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.address = (host, port)
        self.client_socket = socket(AF_INET, SOCK_STREAM)
        self.client_socket.connect(self.address)
        self.receive_thread = Thread(target=self.receive)
        self.receive_thread.start()

    # Handle a new instance of a message
    def receive(self): 
        self.client_socket = socket(AF_INET, SOCK_STREAM)
        self.client_socket.connect(self.address)

        while True:
            try:
                msg = self.client_socket.recv(BUFFER).decode("utf8")
                print(f'{msg}')
            except OSError: 
                break

    # General listener
    def main_loop(self):

        while True:
            message = input()

            if message:
                if message == "/quit":
                    message = message.encode('utf-8')
                    self.client_socket.send(message)
                    self.client_socket.close()
                    break
                else:    
                    message = message.encode('utf-8')
                    self.client_socket.send(message)