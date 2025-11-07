import socket
import threading  # Stage 6 → allows handling multiple connections at the same time

def handle_connection(conn):
    request = conn.recv(1024).decode()
    print("Received:", request)

    words = request.split()

    if len(words) >= 2:
        path = words[1]  

        if path == "/":
            conn.sendall(b"HTTP/1.1 200 OK\r\n\r\n")
        
        elif path.startswith("/echo/"):  
            TheRest = path[len("/echo/"):]  
            response = f"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: {len(TheRest)}\r\n\r\n{TheRest}".encode()
            conn.sendall(response)
        
        elif path == "/user-agent":
            if "User-Agent: " in request:
                parts = request.split("User-Agent: ") 
                user_agent = parts[1].split("\r\n")[0]
            else:
                user_agent = ""
            response = f"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: {len(user_agent)}\r\n\r\n{user_agent}".encode()
            conn.sendall(response)
        
        else:
            conn.sendall(b"HTTP/1.1 404 Not Found\r\n\r\n")

    conn.close()

def main():
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    print("Server running on port 4221...")

    #while loop: accept connections and spawn a thread for each client
    while True:
        conn, addr = server_socket.accept()  # New client connection
        print("New connection:", addr)

        """
        ### What a thread is:
        A thread is like a **mini-program** running inside your main program (the server).
        - You don't create a new server.
        - You don't copy the server.
        - You just let the same server handle multiple things at the same time.
        """

        thread = threading.Thread(target=handle_connection, args=(conn,))
        # threading.Thread(...) → creates a new thread for the client
        # target=handle_connection → this is the function the thread runs
        # args=(conn,) → pass the client socket to the function
        # thread.start() → starts the thread

        thread.start()  # Run the client in a separate thread

# Directly call main() if you want
main()
