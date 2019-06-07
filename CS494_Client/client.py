# Michael Long, Gennadii Sytov -- CS494 -- Client Application -- client_handler implementation

# Imports / Constants
import socket
import threading

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
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(self.address)
        self.connected = True
        # Create a new thread for receiving input
        self.receive_thread = threading.Thread(target=self.receive)
        self.receive_thread.start()

    # Handle receiving a new instance of a message
    def receive(self): 

        # Receive input from the server
        while self.connected:
            # Try to send to the server
            try:
                # Sanitize input
                input = self.client_socket.recv(BUFFER)
                scrub = input.decode("utf8")
                # Close socket if it receives a disconnect message
                if scrub == "--disconnect--":
                    print("You have been disconnected from the server.")
                    self.connected == False
                    return
                # Print any other message sent from the server
                else:
                    print(scrub)

            # Handle a server crash    
            except:
                print("You have been disconnected due to a Server Crash")
                self.connected = False
                return

    # Send messages
    def main_loop(self):

        while self.connected:

            to_send = input()

            if to_send:
                if to_send == "/quit":
                    self.client_socket.send(bytes(to_send, "utf8"))
                    self.client_socket.close()
                    break
                else:    
                    to_send = to_send.encode('utf-8')
                    self.client_socket.send(to_send)