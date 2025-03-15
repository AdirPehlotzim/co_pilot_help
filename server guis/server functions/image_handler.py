import socket
import os

def start_server_image(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print("Server listening on", host, port)

    # Directory to save images
    base_path = os.path.dirname(__file__)
    next_page_path = os.path.join(base_path, "images")
    save_directory = next_page_path
    os.makedirs(save_directory, exist_ok=True)  # Ensure the directory exists

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address} established!")

        # Receive email, name, and password
        email_length = int.from_bytes(client_socket.recv(4), byteorder='big')
        email = client_socket.recv(email_length).decode()

        name_length = int.from_bytes(client_socket.recv(4), byteorder='big')
        name = client_socket.recv(name_length).decode()

        password_length = int.from_bytes(client_socket.recv(4), byteorder='big')
        password = client_socket.recv(password_length).decode()

        print(f"Received email: {email}")
        print(f"Received name: {name}")
        print(f"Received password: {password}")

        # Receive the file name length first
        file_name_length = client_socket.recv(4)
        if not file_name_length:
            break
        file_name_length = int.from_bytes(file_name_length, byteorder='big')

        # Receive the file name
        file_name = client_socket.recv(file_name_length).decode()

        # Construct the full path for saving the image
        save_path = os.path.join(save_directory, f"received_{file_name}")

        # Open the file to save
        with open(save_path, 'wb') as f:
            print(f"Receiving file: {file_name}")
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                f.write(data)

        print(f"File {file_name} received and saved at {save_path}.")
        client_socket.close()

