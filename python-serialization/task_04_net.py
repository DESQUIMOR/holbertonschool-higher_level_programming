import socket
import json

def start_server(host='127.0.0.1', port=65432):
    """
    Starts a server that listens for incoming connections,
    receives serialized JSON data, deserializes it, and prints the dictionary.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"Server listening on {host}:{port}")
        
        conn, addr = server_socket.accept()
        with conn:
            print(f"Connected by {addr}")
            data = conn.recv(1024)
            if data:
                received_dict = json.loads(data.decode('utf-8'))
                print("Received Dictionary from Client:")
                print(received_dict)

def send_data(data, host='127.0.0.1', port=65432):
    """
    Sends a serialized Python dictionary to the server.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        serialized_data = json.dumps(data).encode('utf-8')
        client_socket.sendall(serialized_data)
