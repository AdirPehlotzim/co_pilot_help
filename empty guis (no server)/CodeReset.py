import subprocess
import sys
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox
import os

from DatabaseFunctions import User
from SendEmail import getCodeByEmail, sendMail

path_1 = os.path.dirname(__file__) + r"\assets\frame0"
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(path_1)

email = sys.argv[1]
reason = sys.argv[2]

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def check():
    cur_code = entry_1.get()
    user = User(email)
    if reason == "reset":
        if cur_code == getCodeByEmail(user):
            next_page_path = os.path.dirname(__file__)
            next_page_path = next_page_path.replace(r"code_for_reset\build", "")
            next_page_path = next_page_path + r"newpassword\build\ChangePassword.py"
            subprocess.Popen([sys.executable, next_page_path, email])
        else:
            messagebox.showerror("Wrong code", "The code entered is not the same code, Please enter the same code.")
    if reason == "auth":
        if cur_code == getCodeByEmail(user) :
            if not user.admin:
                next_page_path = os.path.dirname(__file__)
                next_page_path = next_page_path.replace(r"code_for_reset\build", "")
                next_page_path = next_page_path + r"search friend\build\search_friend.py"
                subprocess.Popen([sys.executable, next_page_path, user.email])
            else:
                next_page_path = os.path.dirname(__file__)
                next_page_path = next_page_path.replace(r"code_for_reset\build", "")
                next_page_path = next_page_path + r"admin gui\build\adminGui.py"




                subprocess.Popen([sys.executable, next_page_path, user.email])


        else:
            messagebox.showerror("Wrong code", "The code entered is not the same code, Please enter the same code.")


window = Tk()

window.geometry("413x258")
window.configure(bg="#002849")

canvas = Canvas(
    window,
    bg="#002849",
    height=258,
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
    command=lambda: check(),
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

canvas.create_text(
    8.0,
    121.0,
    anchor="nw",
    text="enter the code you got",
    fill="#000000",
    font=("Staatliches Regular", 20 * -1)
)
window.resizable(False, False)
window.mainloop()
