import os
import sys
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox

from DatabaseFunctions import User
from SendEmail import sendMail

path_1 = os.path.dirname(__file__) + r"\assets\frame0"
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(path_1)


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

import subprocess
def OpenResetPage():
    next_page_path = os.path.dirname(__file__)



def submit():
    email = entry_1.get()
    password = entry_2.get()
    user = User(email)

    if user.password == password:
        next_page_path = os.path.dirname(__file__)
        next_page_path = next_page_path.replace(r"sign in\build", "")
        next_page_path = next_page_path + r"code_for_reset\build\CodeReset.py"
        sendMail(user)
        subprocess.run([sys.executable, "-m", "pip", "install", "opencv-python"])
        subprocess.Popen([sys.executable, next_page_path,email,"auth"])
    else:
        messagebox.showerror("Wrong password", "The code entered is not the same password, Please enter the same password.")

def signUpManagement():
    next_page_path = os.path.dirname(__file__)
    next_page_path = next_page_path.replace(r"sign in\build", "")
    next_page_path = next_page_path + r"sign up\build\SignUpGUI.py"
    subprocess.Popen([sys.executable, next_page_path])


window = Tk()

window.geometry("413x419")
window.configure(bg = "#002849")


canvas = Canvas(
    window,
    bg = "#002849",
    height = 419,
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
    command=lambda: OpenResetPage(),
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

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
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
