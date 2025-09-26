import socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket Request Complete!")
HOST = '127.0.0.1'
PORT = 65432
server_socket.bind((HOST, PORT))
print("Server Ready!")

server_socket.listen(1)
print(f"Server  {HOST}:{PORT} Listen!")
conn, addr = server_socket.accept()

