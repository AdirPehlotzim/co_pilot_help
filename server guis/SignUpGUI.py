import json
import os
import socket
import sys
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, filedialog, messagebox
from pathlib import Path
import subprocess
# Global variable to track the image path
selected_image_path = ""

# Relative path to assets (no changes here)
path_1 = os.path.dirname(__file__) + r"\assets\frame0"
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(path_1)
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def uploadImage():
    global selected_image_path
    selected_image_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif")])
    print(selected_image_path)


def send_request(action, data):
    host = '127.0.0.1'  # Server address
    port = 65432  # Port number

    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))

        request_data = {'action': action, **data}
        client_socket.send(json.dumps(request_data).encode('utf-8'))

        response = client_socket.recv(1024).decode('utf-8')
        response_data = json.loads(response)

        client_socket.close()
        return response_data

    except ConnectionRefusedError:
        messagebox.showerror("Connection Error", "Failed to connect to the server. Please try again.")
        return {"status": "error", "message": "Server unreachable"}

start_image_server_data = {}
send_request('start_image_server', start_image_server_data)

def send_image(image_path, email, name, password, host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    # Send email, name, and password
    client_socket.send(len(email).to_bytes(4, byteorder='big'))
    client_socket.send(email.encode())
    client_socket.send(len(name).to_bytes(4, byteorder='big'))
    client_socket.send(name.encode())
    client_socket.send(len(password).to_bytes(4, byteorder='big'))
    client_socket.send(password.encode())

    # Get the file name
    file_name = os.path.basename(image_path)

    # Send the file name length and file name
    client_socket.send(len(file_name).to_bytes(4, byteorder='big'))
    client_socket.send(file_name.encode())

    # Open the image file and send its content
    with open(image_path, 'rb') as f:
        print(f"Sending file: {file_name}")
        while (data := f.read(1024)):
            client_socket.send(data)

    print(f"File {file_name} sent.")
    client_socket.close()

def submit():
    print("The image is: " + selected_image_path)
    email = entry_2.get().strip()
    name = entry_3.get().strip()
    password = entry_1.get().strip()

    if not email or not name or not password:
        messagebox.showerror("Error", "All fields are required.")
        return

    if not selected_image_path:
        messagebox.showerror("Error", "Upload a profile picture")
        return

    # Server details
    host = '127.0.0.1'
    port = 12345
    # Call the send_image function to send data
    send_image(selected_image_path, email, name, password, host, port)

    # Optionally, show success message
    messagebox.showinfo("Success", "Details and image sent successfully!")
    base_path = os.path.dirname(__file__)
    base_path = os.path.abspath(os.path.join(base_path, "..", ".."))
    next_page_path = os.path.join(base_path, "sign in", "build", "SignIn.py")
    subprocess.Popen([sys.executable, next_page_path])
    window.destroy()

window = Tk()

window.geometry("413x392")
window.configure(bg = "#002849")


canvas = Canvas(
    window,
    bg = "#002849",
    height = 392,
    width = 413,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    206.0,
    60.0,
    image=image_image_1
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: submit(),
    relief="flat"
)
button_1.place(
    x=9.0,
    y=360.0,
    width=379.93695068359375,
    height=26.0
)

canvas.create_rectangle(
    4.0,
    157.0,
    398.0,
    158.0000343571512,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    9.0,
    272.0,
    37.0,
    304.0,
    fill="#235786",
    outline="")

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    209.5,
    288.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#0D397A",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=37.0,
    y=272.0,
    width=345.0,
    height=30.0
)

canvas.create_text(
    9.0,
    258.0,
    anchor="nw",
    text="Password",
    fill="#FFFFFF",
    font=("Staatliches Regular", 12 * -1)
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    23.0,
    288.0,
    image=image_image_2
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=354.0,
    y=279.0,
    width=23.0,
    height=19.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    209.5,
    193.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#0D397A",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=37.0,
    y=177.0,
    width=345.0,
    height=30.0
)

canvas.create_rectangle(
    9.0,
    177.0,
    37.0,
    209.0,
    fill="#235786",
    outline="")

canvas.create_text(
    9.0,
    163.0,
    anchor="nw",
    text="Email",
    fill="#FFFDFD",
    font=("Staatliches Regular", 12 * -1)
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    23.0,
    193.0,
    image=image_image_3
)

canvas.create_text(
    8.0,
    121.0,
    anchor="nw",
    text="enter details below to sign up ",
    fill="#000000",
    font=("Staatliches Regular", 24 * -1)
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    209.5,
    239.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#0D397A",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=37.0,
    y=223.0,
    width=345.0,
    height=30.0
)

canvas.create_rectangle(
    9.0,
    223.0,
    37.0,
    255.0,
    fill="#235786",
    outline="")

canvas.create_text(
    9.0,
    209.0,
    anchor="nw",
    text="Name",
    fill="#FFFDFD",
    font=("Staatliches Regular", 12 * -1)
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    23.0,
    239.0,
    image=image_image_4
)

canvas.create_text(
    9.0,
    307.0,
    anchor="nw",
    text="profile image",
    fill="#FFFDFD",
    font=("Staatliches Regular", 12 * -1)
)

canvas.create_rectangle(
    9.0,
    321.0,
    37.0,
    353.0,
    fill="#235786",
    outline="")

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: uploadImage(),
    relief="flat"
)
button_3.place(
    x=14.0,
    y=328.0,
    width=18.0,
    height=18.0
)
window.resizable(False, False)
window.mainloop()