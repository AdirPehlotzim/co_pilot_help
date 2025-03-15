import os
import sys
from PIL import Image, ImageTk
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox
from DatabaseFunctions import User

main_user =  User(sys.argv[1])
friend_user = User(sys.argv[2])
path_1 = os.path.dirname(__file__) + r"\assets\frame0"
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(path_1)


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def get_path(user):
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # עבור 3 תיקיות אחורה כדי להגיע ל-cyber-project
    project_root = os.path.abspath(os.path.join(script_dir, "..", "..", ".."))

    # צרף את "images" לנתיב של הפרויקט
    images_dir = os.path.join(project_root, "images")

    # צרף את שם התמונה של המשתמש
    user1 = os.path.join(images_dir, user.profile_picture)

    # נרמל את הנתיב כדי למנוע שגיאות במערכות הפעלה שונות
    user1 = os.path.normpath(user1)
    return user1






window = Tk()

window.geometry("1140x641")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 641,
    width = 1140,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    1140.0,
    641.25,
    fill="#002849",
    outline="")


canvas.create_rectangle(
    257.09375,
    0.0,
    1140.0,
    59.375,
    fill="#0D397A",
    outline="")


canvas.create_text(
    320.8125,
    1.1873779296875,
    anchor="nw",
    text=friend_user.name,
    fill="#FFFFFF",
    font=("Staatliches Regular", 23 * -1)
)



canvas.create_text(
    96.78125,
    16.0313720703125,
    anchor="nw",
    text=main_user.name,
    fill="#FFFFFF",
    font=("Staatliches Regular", 23 * -1)
)

canvas.create_rectangle(
    276.6875,
    564.0625,
    1125.7499389648438,
    613.9375,
    fill="#D9D9D9",
    outline="")



canvas.create_rectangle(
    547.4375,
    485.6875,
    1125.75,
    535.5625,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    548.0311889648438,
    328.9375,
    1126.3436889648438,
    378.8125,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    548.0311889648438,
    328.9375,
    1126.3436889648438,
    378.8125,
    fill="#D9D9D9",
    outline="")

canvas.create_text(
    964.25,
    535.5625,
    anchor="nw",
    text="sent 14:14",
    fill="#000000",
    font=("Staatliches Regular", 23 * -1)
)

canvas.create_text(
    722.0,
    458.375,
    anchor="nw",
    text="sent 14:13",
    fill="#000000",
    font=("Staatliches Regular", 23 * -1)
)


canvas.create_rectangle(
    280.84375,
    406.71875,
    859.15625,
    456.59375,
    fill="#3A6CA6",
    outline="")

canvas.create_text(
    993.9375,
    379.40625,
    anchor="nw",
    text="sent 14:12",
    fill="#000000",
    font=("Staatliches Regular", 23 * -1)
)

canvas.create_rectangle(
    1129.90625,
    58.78125,
    1138.21875,
    71.25,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    -1.7812498807907104,
    93.81250011920929,
    257.09375,
    95.59375,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    -1.7812498807907104,
    93.81250011920929,
    257.09375,
    95.59375,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    -1.7812498807907104,
    57.593750157378054,
    1139.9999861717079,
    59.96875,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    255.31247208928153,
    -1.7812498807907104,
    257.09375,
    641.25,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    238.0937501192093,
    93.81253063678741,
    239.87502039955882,
    562.28125,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    1138.2187501192093,
    -0.5937498807907104,
    1140.0000025953639,
    60.5625,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    -1.7812498807907104,
    562.2812501192093,
    257.09375,
    564.0625,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    1128.71875,
    57.000030517578125,
    1129.90625,
    564.0625,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    1138.2187501192093,
    56.406280636787415,
    1140.0,
    564.0625,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    1139.40625,
    0.59405517578125,
    1140.000002595365,
    566.4381103515625,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    256.5,
    563.4687499999998,
    1140.0,
    564.0625,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    1128.71875,
    57.0,
    1138.21875,
    58.1875,
    fill="#050505",
    outline="")




# תמונת המשתמש הראשי
main_user_img_path = os.path.normpath(get_path(main_user))
main_user_img = Image.open(relative_to_assets(main_user_img_path))
main_user_resized = main_user_img.resize((55, 55), Image.LANCZOS)  # שימוש ב-LANCZOS במקום ANTIALIAS
# המרת התמונה לפורמט המתאים ל-Tkinter
main_user_tk_image = ImageTk.PhotoImage(main_user_resized)
# הוספת התמונה לקנבס במקום המתאים
main_user_image_canvas = canvas.create_image(
    0.0, 0.0,  # מיקום בפינה השמאלית העליונה
    anchor="nw",
    image=main_user_tk_image
)
# שמירה על רפרנס כדי שהתמונה לא תיעלם
canvas.main_user_image = main_user_tk_image

# תמונת המשתמש החבר
friend_user_img_path = os.path.normpath(get_path(friend_user))
friend_user_img = Image.open(relative_to_assets(friend_user_img_path))
friend_user_resized = friend_user_img.resize((55, 55), Image.LANCZOS)  # שימוש ב-LANCZOS במקום ANTIALIAS
# המרת התמונה לפורמט המתאים ל-Tkinter
friend_user_tk_image = ImageTk.PhotoImage(friend_user_resized)
# הוספת התמונה לקנבס במקום המתאים
friend_user_image_canvas = canvas.create_image(
    260.0, 0.0,  # מיקום חדש עבור התמונה של החבר
    anchor="nw",
    image=friend_user_tk_image
)
# שמירה על רפרנס כדי שהתמונה לא תיעלם
canvas.friend_user_image = friend_user_tk_image


entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    695.0,
    589.25,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=330.0,
    y=565.25,
    width=730.0,
    height=46.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=1087.0,
    y=8.25,
    width=43.0,
    height=43.0
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
    x=291.0,
    y=573.25,
    width=33.0,
    height=33.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=1082.0,
    y=576.25,
    width=27.0,
    height=27.0
)

canvas.create_text(
    300.0,
    416.25,
    anchor="nw",
    text="{MESSAGE}",
    fill="#FFFFFF",
    font=("Staatliches Regular", 24 * -1)
)

canvas.create_text(
    570.0,
    336.25,
    anchor="nw",
    text="{MESSAGE}",
    fill="#467DBB",
    font=("Staatliches Regular", 24 * -1)
)

canvas.create_text(
    570.0,
    496.25,
    anchor="nw",
    text="{MESSAGE}",
    fill="#467DBB",
    font=("Staatliches Regular", 24 * -1)
)
window.resizable(False, False)
window.mainloop()
