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


if len(words) >= 2:
    path = words[1]  # The URL path

    
    if path == "/":
        conn.sendall(b"HTTP/1.1 200 OK\r\n\r\n")
    
    
    elif path.startswith("/echo/"): #if the Path start with:/echo/
        # Extract the string after /echo/
        TheRest = path[len("/echo/"):] #we send the rest of the path in the response
        # Build response with headers and body
        response = f"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: {len(TheRest)}\r\n\r\n{TheRest}".encode()
        # encode to bytes
        conn.sendall(response)
    
    # --- Any other path ---
    else:
        conn.sendall(b"HTTP/1.1 404 Not Found\r\n\r\n")

conn.close()
