import os
import sys
from DatabaseFunctions import User, get_user_by_name
import subprocess
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox
path_1 = os.path.dirname(__file__) + r"\assets\frame0"
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(path_1)

# main user must be string, it's the sys.argv[1]
main_user = sys.argv[1]
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()
window.geometry("420x258")
window.configure(bg="#002849")

def submit():
    friend_name = entry_1.get()
    if get_user_by_name(friend_name):
        next_page_path = os.path.dirname(__file__)
        next_page_path = next_page_path.replace(r"gui\search friend\build", "")
        next_page_path = next_page_path + r"gui\CHAT GUI\build\ChatGUI.py"
        friend_user = get_user_by_name(friend_name).email
        venv_path = sys.executable

        # Pass main_user and friend_user as arguments to the subprocess
        subprocess.Popen([venv_path, next_page_path, main_user, friend_user], env=os.environ)
    else:
        messagebox.showerror("Error", "Your friend doesn't exist")


canvas = Canvas(
    window,
    bg="#002849",
    height=258,
    width=420,
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
    command=lambda: submit(),
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

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    39.0,
    163.0,
    image=image_image_2
)

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

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    25.0,
    187.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    63.0,
    133.0,
    image=image_image_4
)
window.resizable(False, False)
window.mainloop()
