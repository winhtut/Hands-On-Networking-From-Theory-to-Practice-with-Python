import socket
HOST = '127.0.0.1'
PORT = 65432
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client_socket.connect((HOST, PORT))
    print(f"Server {HOST}:{PORT} connected!")
    message = "Hello, World!"
    client_socket.sendall(message.encode('utf-8'))
    data = client_socket.recv(1024)
    print(f"From Server: {data.decode('utf-8')}")
    client_socket.close()
except ConnectionRefusedError:
    print("Error!")
    exit()


