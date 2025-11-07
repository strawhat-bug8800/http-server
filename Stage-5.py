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
    
    
    elif path.startswith("/echo/"):  # if the Path starts with /echo/
        TheRest = path[len("/echo/"):]  # Extract the string after /echo/
        # Build response with headers and body
        response = f"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: {len(TheRest)}\r\n\r\n{TheRest}".encode()
        conn.sendall(response)
    
    
    elif path == "/user-agent":
        
        if "User-Agent: " in request:
            # Step 1: Split the request at "User-Agent: "
            parts = request.split("User-Agent: ") #return a list 

            # After splitting, 'parts' is a list of 2 strings:
            # parts[0]  everything before "User-Agent:"
            # parts[1]  everything after "User-Agent:" including the value we want 'the value of the user agent'

            # Step 2: Split the second part at the first CRLF "\r\n" to isolate the value
            user_agent = parts[1].split("\r\n")[0]
            # Now 'user_agent' contains only the User-Agent value, e.g., 'curl/7.64.1'

            """
            Example:
            request = "GET / HTTP/1.1\r\nHost: localhost\r\nUser-Agent: curl/7.64.1\r\n\r\n"

            parts = request.split("User-Agent: ")
            # parts[0] = "GET / HTTP/1.1\r\nHost: localhost\r\n"
            # parts[1] = "curl/7.64.1\r\n\r\n"

            user_agent = parts[1].split("\r\n")[0]
            # user_agent = "curl/7.64.1"
            """ 
        else:
            user_agent = ""
        # Build response with headers and body
        response = f"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: {len(user_agent)}\r\n\r\n{user_agent}".encode()
        conn.sendall(response)
    
    # --- Any other path ---
    else:
        conn.sendall(b"HTTP/1.1 404 Not Found\r\n\r\n")

conn.close()
