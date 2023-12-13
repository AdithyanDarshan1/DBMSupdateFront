
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\programs\VS code\C programming\S5DBMS\build7\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("900x600")
window.configure(bg = "#1F43A0")


canvas = Canvas(
    window,
    bg = "#1F43A0",
    height = 600,
    width = 900,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    390.0,
    45.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    60.0,
    44.0,
    image=image_image_2
)

canvas.create_text(
    100.0,
    7.0,
    anchor="nw",
    text="SEARCH ACCOUNT ",
    fill="#000000",
    font=("Inter Bold", 40 * -1)
)

canvas.create_rectangle(
    44.0,
    128.0,
    506.0,
    503.0,
    fill="#AEBFFF",
    outline="")

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
    x=389.0,
    y=527.0,
    width=155.0,
    height=44.0
)

canvas.create_text(
    560.0,
    257.0,
    anchor="nw",
    text="ENTER ACCOUNT NO.",
    fill="#FFFFFF",
    font=("Inter Bold", 26 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    684.0,
    315.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=550.0,
    y=297.0,
    width=268.0,
    height=35.0
)

canvas.create_text(
    75.0,
    177.0,
    anchor="nw",
    text="Account no:",
    fill="#000000",
    font=("Inter Bold", 26 * -1)
)

canvas.create_text(
    80.0,
    221.0,
    anchor="nw",
    text="User Name:",
    fill="#000000",
    font=("Inter Bold", 26 * -1)
)

canvas.create_text(
    100.0,
    265.0,
    anchor="nw",
    text="Phone No:",
    fill="#000000",
    font=("Inter Bold", 26 * -1)
)

canvas.create_text(
    152.0,
    311.0,
    anchor="nw",
    text="Email:",
    fill="#000000",
    font=("Inter Bold", 26 * -1)
)

canvas.create_text(
    115.0,
    353.0,
    anchor="nw",
    text="Address:",
    fill="#000000",
    font=("Inter Bold", 26 * -1)
)

canvas.create_text(
    169.0,
    397.0,
    anchor="nw",
    text="Age:",
    fill="#000000",
    font=("Inter Bold", 26 * -1)
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    352.0,
    315.0,
    image=image_image_3
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
    x=829.0,
    y=297.0,
    width=39.0,
    height=39.0
)
window.resizable(False, False)
window.mainloop()
