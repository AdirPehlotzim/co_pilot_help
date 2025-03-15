import os
import socket
import threading
import json
from SendEmail import sendMail, getCodeByEmail
from DatabaseFunctions import User, change_user_password, AddUser, UserExist, get_user_by_name, remove_user_by_email, \
    grant_admin, get_all_users_details
from log_management import writing_in_log

# Server setup
HOST = '127.0.0.1'
PORT = 65432
print("Image Server listening on", HOST, PORT)
print(f"Server listening on {HOST}:{PORT}")

# Ensure the image directory exists
base_path = os.path.dirname(__file__)
IMAGE_SAVE_DIR = os.path.join(base_path, "images")
if not os.path.exists(IMAGE_SAVE_DIR):
    os.makedirs(IMAGE_SAVE_DIR)


def terminal_interface():
    while True:
        command = input("Enter a command (type 'exit' to quit , help for commands list):  \n")

        if command == "help":
            print(
                "addAdmin *email* - promote a user to be an admin \n *removeAdmin *email* - remove admin to a user \nuserList - listing all the users from the database \n exit - shutdown the server \n ")

        elif command == 'exit':
            print("Shutting down the server.")
            break
        elif command == 'list users':
            print(get_all_users_details())
        elif "addAdmin" in command:
            # Get the email from the command
            parts = command.split()
            if len(parts) < 2:
                print("Error: Please provide the email address.")
            else:
                user_email = parts[1]  # Get the email from the command (second part)
                try:
                    user_main = User(user_email)  # Create User object with the email
                    user_main.admin = True  # Promote to admin
                    print(f"{user_email} has been promoted to admin.")
                except Exception as e:
                    print(f"Error: {e}")
        elif "removeAdmin" in command:
            # Get the email from the command
            parts = command.split()
            if len(parts) < 2:
                print("Error: Please provide the email address.")
            else:
                user_email = parts[1]  # Get the email from the command (second part)
                try:
                    user_main = User(user_email)  # Create User object with the email
                    user_main.admin = False  # Promote to admin
                    print(f"{user_email} IS longer an admin.")
                except Exception as e:
                    print(f"Error: {e}")
        else:
            print(f"Unknown command: {command}")


# Start terminal interface in a separate thread
threading.Thread(target=terminal_interface, daemon=True).start()


def start_server_image(host, port):
    # This function should run in a separate thread so it doesn't block the main server loop
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    # Directory to save images
    save_directory = IMAGE_SAVE_DIR
    os.makedirs(save_directory, exist_ok=True)

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
        AddUser(email, password, name, file_name)

        client_socket.close()


def handle_client(client_socket):
    try:
        # Receive metadata (JSON)
        request = client_socket.recv(1024).decode('utf-8')
        data = json.loads(request)

        response = {"status": "error", "message": "Unknown action"}

        if data['action'] == 'authenticate':
            email = data['email']
            password = data['password']
            user = User(email)
            if user and user.password == password:
                response = {"status": "success", "message": "Authentication successful"}
            else:
                response = {"status": "error", "message": "Invalid credentials"}

        elif data['action'] == 'start_image_server':
            # Start the image server in a separate thread
            threading.Thread(target=start_server_image, args=(HOST, 12345)).start()

        elif data['action'] == 'verify_code':
            email = data['email']
            entered_code = data['code']
            correct_code = getCodeByEmail(user=User(email))
            if entered_code == correct_code:
                user = User(email)
                response = {"status": "success", "message": "Code verified successfully", "is_admin": user.admin}
                print(user.admin)
            else:
                response = {"status": "error", "message": "Invalid verification code"}

        elif data['action'] == 'change_password':
            email = data['email']
            password = data['password']
            user = User(email)
            if user:
                change_user_password(email, password)
                response = {"status": "success", "message": "Password changed successfully"}
            else:
                response = {"status": "error", "message": "User not found"}

        elif data['action'] == 'send_email':
            email = data['email']
            user = User(email)
            if sendMail(user):
                response = {"status": "success", "message": "Email sent"}
            else:
                response = {"status": "error", "message": "Failed to send email"}



        elif data['action'] == 'search_friend':
            friend_name = data['friend_name']
            friend_user = get_user_by_name(friend_name)
            if friend_user:
                response = {"status": "success", "message": "Friend found", "friend_user": friend_user.email}
            else:
                response = {"status": "error", "message": "Friend does not exist"}

        elif data['action'] == 'remove_user':
            email_to_remove = data['email']
            admin_email = data['admin_email']
            response = {"status": "success", "message": f"User {email_to_remove} has been removed by {admin_email}"}


        # Send the response back to the client
        client_socket.send(json.dumps(response).encode('utf-8'))

    except Exception as e:
        print(f"Error: {e}")
        response = {"status": "error", "message": "An error occurred"}
        client_socket.send(json.dumps(response).encode('utf-8'))

    finally:
        client_socket.close()


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connected to {client_address}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()


if __name__ == '__main__':
    start_server()
