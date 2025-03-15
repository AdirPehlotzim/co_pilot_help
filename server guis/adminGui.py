import os
import sys
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox

import socket
import json

path_1 = os.path.dirname(__file__) + r"\assets\frame0"
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(path_1)
admin_email = sys.argv[1]

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


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


def remove_user_final():
    email_to_remove = entry_1.get()
    response = send_request('remove_user', {'email': email_to_remove, 'admin_email': admin_email})

    if response['status'] == 'success':
        messagebox.showinfo("User Removed", response['message'])
    else:
        messagebox.showerror("Error", response['message'])


window = Tk()

window.geometry("413x258")
window.configure(bg = "#002849")


canvas = Canvas(
    window,
    bg = "#002849",
    height = 258,
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
    command=lambda: remove_user_final(),
    relief="flat"
)
button_1.place(
    x=11.0,
    y=216.0,
    width=378.0,
    height=23.783782958984375
)

canvas.create_rectangle(
    5.0,
    153.0,
    398.0,
    153.0000343571512,
    fill="#000000",
    outline="")

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    211.5,
    187.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#0D397A",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=39.0,
    y=171.0,
    width=345.0,
    height=30.0
)

canvas.create_rectangle(
    11.0,
    171.0,
    39.0,
    203.0,
    fill="#235786",
    outline="")

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    25.0,
    187.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    100.0,
    133.0,
    image=image_image_3
)
window.resizable(False, False)
window.mainloop()
