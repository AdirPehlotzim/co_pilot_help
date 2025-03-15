import os
import subprocess
import sys
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox
import socket
import json

path_1 = os.path.dirname(__file__) + r"\assets\frame0"
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(path_1)


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


email = sys.argv[1]


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


def changePassword():
    password_1 = entry_1.get()
    password_2 = entry_2.get()

    if password_1 == password_2:
        response = send_request('change_password', {'email': email, 'password': password_1})

        if response['status'] == 'success':
            messagebox.showinfo("Password Changed", response['message'])
            base_path = os.path.dirname(__file__)
            base_path = os.path.abspath(os.path.join(base_path, "..", ".."))
            next_page_path = os.path.join(base_path, "sign in", "build", "SignIn.py")
            subprocess.Popen([sys.executable, next_page_path])
            window.destroy()
        else:
            messagebox.showerror("Error", response['message'])
    else:
        messagebox.showerror("Wrong code", "The passwords do not match. Please enter the same password twice.")


window = Tk()

window.geometry("413x281")
window.configure(bg="#002849")

canvas = Canvas(
    window,
    bg="#002849",
    height=281,
    width=413,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
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
    command=lambda: changePassword(),
    relief="flat"
)
button_1.place(
    x=11.0,
    y=252.0,
    width=378.0,
    height=23.783782958984375
)

canvas.create_rectangle(
    8.0,
    143.0,
    401.0,
    143.0000343571512,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    8.0,
    245.99996948242188,
    401.0,
    246.00000383957308,
    fill="#000000",
    outline="")

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    211.5,
    178.0,
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
    y=162.0,
    width=345.0,
    height=30.0
)

canvas.create_rectangle(
    11.0,
    162.0,
    39.0,
    194.0,
    fill="#235786",
    outline="")

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    25.0,
    178.0,
    image=image_image_2
)

canvas.create_text(
    8.0,
    121.0,
    anchor="nw",
    text="reset your password",
    fill="#000000",
    font=("Staatliches Regular", 20 * -1)
)

canvas.create_text(
    11.0,
    147.0,
    anchor="nw",
    text="enter new password",
    fill="#000000",
    font=("Staatliches Regular", 12 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    211.5,
    225.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#0D397A",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=39.0,
    y=209.0,
    width=345.0,
    height=30.0
)

canvas.create_rectangle(
    11.0,
    209.0,
    39.0,
    241.0,
    fill="#235786",
    outline="")

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    25.0,
    225.0,
    image=image_image_3
)

canvas.create_text(
    11.0,
    194.0,
    anchor="nw",
    text="reenter new password",
    fill="#000000",
    font=("Staatliches Regular", 12 * -1)
)
window.resizable(False, False)
window.mainloop()
