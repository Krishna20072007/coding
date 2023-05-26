import socket
import threading

# Global variables
HOST = '127.0.0.1'  # Server IP address
PORT = 5000  # Server port number

# Function to receive and display messages from the server
def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            print(message)
        except:
            print('An error occurred while receiving the message.')
            client_socket.close()
            break

# Main client function
def run_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    print('Connected to the server.')

    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    while True:
        message = input("Message: ")
        if message.lower() == 'quit':
            break
        try:
            client_socket.send(message.encode('utf-8'))
        except:
            print('An error occurred while sending the message.')
            break

    client_socket.close()

# Start the client
run_client()
