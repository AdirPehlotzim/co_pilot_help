import os
import sys
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox
import socket
import json
import subprocess

path_1 = os.path.dirname(__file__) + r"\assets\frame0"
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(path_1)


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


def submit():
    email = entry_1.get()
    password = entry_2.get()  # ✅ FIXED: Now correctly gets password from entry_2
    response = send_request('authenticate', {'email': email, 'password': password})

    if response['status'] == 'success':
        messagebox.showinfo("Login Successful", response['message'])

        # ✅ **Send an email with the verification code**
        email_response = send_request('send_email', {'email': email})

        if email_response['status'] == 'success':
            messagebox.showinfo("Email Sent", "A verification code has been sent to your email.")
        else:
            messagebox.showerror("Error", email_response['message'])
            return  # 🚨 Stop if email fails to send

        base_path = os.path.dirname(__file__)

        # Navigate up one level to remove "sign in/build"
        base_path = os.path.abspath(os.path.join(base_path, "..", ".."))  # Move up two levels

        # Now correctly set the path to CodeReset.py
        next_page_path = os.path.join(base_path, "code_for_reset", "build", "CodeReset.py")

        subprocess.Popen([sys.executable, next_page_path, email, "auth"])
        window.destroy()  # ✅ Close current window
    else:
        messagebox.showerror("Error", response['message'])

def signUpManagement():
    base_path = os.path.dirname(__file__)
    base_path = os.path.abspath(os.path.join(base_path, "..", ".."))
    next_page_path = os.path.join(base_path, "sign up", "build", "SignUpGUI.py")
    subprocess.Popen([sys.executable, next_page_path])


def forgotPassword():
    base_path = os.path.dirname(__file__)
    base_path = os.path.abspath(os.path.join(base_path, "..", ".."))
    next_page_path = os.path.join(base_path, "forgot password", "build", "PasswordGUI.py")
    subprocess.Popen([sys.executable, next_page_path])
    window.destroy()


window = Tk()

window.geometry("413x419")
window.configure(bg="#002849")

canvas = Canvas(
    window,
    bg="#002849",
    height=419,
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

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    208.5,
    226.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#0D397A",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=36.0,
    y=210.0,
    width=345.0,
    height=30.0
)

canvas.create_rectangle(
    8.0,
    210.0,
    36.0,
    242.0,
    fill="#235786",
    outline="")

canvas.create_rectangle(
    9.0,
    260.0,
    37.0,
    292.0,
    fill="#235786",
    outline="")

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    209.5,
    276.0,
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
    y=260.0,
    width=345.0,
    height=30.0
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
    x=8.0,
    y=305.0,
    width=379.8968505859375,
    height=26.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: signUpManagement(),
    relief="flat"
)
button_2.place(
    x=8.0,
    y=350.0,
    width=379.93695068359375,
    height=26.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))

button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: forgotPassword(),
    relief="flat"
)
button_3.place(
    x=9.0,
    y=384.0,
    width=378.0,
    height=23.783782958984375
)

canvas.create_rectangle(
    4.0,
    341.0,
    401.0,
    342.0000346194195,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    7.0,
    191.0,
    401.0,
    192.0000343571512,
    fill="#000000",
    outline="")

canvas.create_text(
    8.0,
    196.0,
    anchor="nw",
    text="Email",
    fill="#FFFDFD",
    font=("Staatliches Regular", 12 * -1)
)

canvas.create_text(
    9.0,
    246.0,
    anchor="nw",
    text="Password",
    fill="#FFFFFF",
    font=("Staatliches Regular", 12 * -1)
)

# Variable to track password visibility
# Variable to track password visibility
password_visible = False

def toggle_password():
    global password_visible
    if password_visible:
        entry_2.config(show="*")  # Hide password
    else:
        entry_2.config(show="")  # Show password
    password_visible = not password_visible  # Toggle state



entry_2 = Entry(
    bd=0,
    bg="#0D397A",
    fg="#000716",
    highlightthickness=0,
    show="*"  # ✅ Hides password by default
)
entry_2.place(
    x=37.0,
    y=260.0,
    width=345.0,
    height=30.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: toggle_password(),
    relief="flat"
)
button_4.place(
    x=354.0,
    y=267.0,
    width=23.0,
    height=19.0
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    23.0,
    276.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    22.0,
    226.0,
    image=image_image_3
)

canvas.create_text(
    8.0,
    121.0,
    anchor="nw",
    text="Welcome Back!\nWe’re happy to see you, sign in below.",
    fill="#FFFFFF",
    font=("Inter", 12 * -1)
)
window.resizable(False, False)
window.mainloop()
