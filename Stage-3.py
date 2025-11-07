import socket

server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
print("Server running on port 4221...")

conn, addr = server_socket.accept()
print("New connection:", addr)

# Receive request
request = conn.recv(1024).decode()
print("Received:", request)




# Split request into words (METHOD, PATH, VERSION)
words = request.split()

# .split() → splits a string into a list of words, separated by whitespace by default
"""Example:
# request = "GET /index.html HTTP/1.1\r\nHost: localhost\r\n\r\n"
# words = request.split() 
# words will be: ['GET', '/index.html', 'HTTP/1.1', 'Host:', 'localhost']
# So:
#  words[0] = 'GET' (METHOD)
#  words[1] = '/index.html (path)
#  words[2] = 'HTTP/1.1' (version)
"""

if len(words) >= 2:
    path = words[1]  # The URL path

    if path == "/":
        # Respond with 200 OK
        conn.sendall(b"HTTP/1.1 200 OK\r\n\r\n")
    else:
        # Respond with 404 Not Found
        conn.sendall(b"HTTP/1.1 404 Not Found\r\n\r\n")

conn.close()
