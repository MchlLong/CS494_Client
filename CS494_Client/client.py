# Michael Long, Gennadii Sytov -- CS494 -- Client Application -- Server Class

# Imports / Constants
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
BUFFER = 1024

# Designed to handle each of the server interactions for the client
class client_handler():

    # Init
    def __init__(self, host, port):
        # Basic socket setup
        self.host = host
        self.port = port
        self.address = (host, port)
        # Attempt to bind to socket
        self.client_socket = socket(AF_INET, SOCK_STREAM)
        self.client_socket.connect(self.address)
        self.connected = True
        # Create a new thread for receiving input
        self.receive_thread = Thread(target=self.receive)
        self.receive_thread.start()

    # Handle a new instance of a message
    def receive(self): 

        while self.connected:
            try:
                msg = self.client_socket.recv(BUFFER)
                scrub = msg.decode("utf8")
                if scrub == "You have been disconnected from the server.":
                    print(scrub)
                    self.connected == False
                    return
                else:
                    print(scrub)

                
            except OSError: 
                self.connected = False
                return

    # General listener
    def main_loop(self):

        while self.connected:

            message = input()

            if message:
                if message == "/quit":
                    self.client_socket.send(bytes(message, "utf8"))
                    self.client_socket.close()
                    break
                else:    
                    message = message.encode('utf-8')
                    self.client_socket.send(message)