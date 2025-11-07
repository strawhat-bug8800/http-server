import socket

server_socket = socket.create_server(("localhost", 4221), reuse_port=True)


print("Server running on port 4221...")
conn, addr = server_socket.accept()
print("New connection:", addr)



request = conn.recv(1024).decode()
print("Received:", request)



conn.sendall(b"HTTP/1.1 200 OK\r\n\r\n")


conn.close()
