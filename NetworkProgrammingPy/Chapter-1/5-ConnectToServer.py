import socket
HOST = '127.0.0.1'
PORT = 65432
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client_socket.connect((HOST, PORT))
    print(f"Server {HOST}:{PORT} connected!")
except ConnectionRefusedError:
    print("Error!")
    exit()

