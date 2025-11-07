import socket


# We can create a server socket like a “classic” socket:
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Then we would need to bind it to an IP & port using bind()
# and call listen() to start listening for incoming connections.
# socket.create_server() does all of this in one step.


server_socket = socket.create_server(("localhost", 4221), reuse_port=True)

# Create a TCP server socket.
# "localhost" = 127.0.0.1 → only applications on this machine can connect
# if you wanted other machines to connect, you’d use "0.0.0.0" (all interfaces) instead.
# reuse_port=True → allows restarting the server immediately without "address in use" errors
# socket.create_server() is a shortcut: it creates the socket, binds it, and starts listening in one step
print("Server running on port 4221...")


# Each time a client connects to the server, accept() returns a new socket object `conn`
# that we use to communicate with that specific client.
# `addr` stores the client’s address (IP and port).
conn, addr = server_socket.accept()
print("New connection:", addr)


# Receive data from the client. recv() returns bytes, so we use decode() to convert it to a string.
request = conn.recv(1024).decode()
print("Received:", request)


# Send a simple HTTP response to the client.
# The b"" means the string is converted to bytes, which is required by sendall().
conn.sendall(b"HTTP/1.1 200 OK\r\n\r\n")

# Close the connection after sending the response.
conn.close()
