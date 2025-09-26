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

with conn:
    print(f"Client {addr} Connected!")
    data = conn.recv(1024)
    print(f"Accepted Message: {data.decode('utf-8')}")

    response = "Welcome to Server"
    conn.sendall(response.encode('utf-8'))