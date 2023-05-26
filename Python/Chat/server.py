import socket
import threading

# Global variables
HOST = '127.0.0.1'  # Server IP address
PORT = 5001  # Server port number
clients = []  # List of connected clients
lock = threading.Lock()  # Lock to synchronize access to shared data

# Function to handle client connections
def handle_client(client_socket, client_address):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                broadcast_message(message)
            else:
                remove_client(client_socket)
                break
        except:
            remove_client(client_socket)
            break

# Function to broadcast message to all connected clients
def broadcast_message(message):
    with lock:
        for client in clients:
            client.send(message.encode('utf-8'))

# Function to remove client from the list
def remove_client(client_socket):
    with lock:
        if client_socket in clients:
            clients.remove(client_socket)

# Main server function
def run_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print('Server started and listening on {}:{}'.format(HOST, PORT))

    while True:
        client_socket, client_address = server_socket.accept()
        with lock:
            clients.append(client_socket)
        print('New client connected: {}'.format(client_address))

        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

# Start the server
run_server()
