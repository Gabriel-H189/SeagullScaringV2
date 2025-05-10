from configparser import ConfigParser
from datetime import datetime
from os.path import isdir
from random import randint, seed
from sys import exit as sys_exit
from threading import Thread
from time import perf_counter, sleep
from tkinter import END, VERTICAL, WORD
from tkinter.messagebox import askyesno, showinfo, showwarning  # type: ignore
from tkinter.simpledialog import askstring
from typing import Any
from webbrowser import open_new
from zipfile import ZipFile

from customtkinter import (  # type: ignore
    DISABLED,
    CTk,
    CTkButton,
    CTkComboBox,
    CTkEntry,
    CTkImage,
    CTkLabel,
    CTkScrollbar,
    CTkSlider,
    CTkTextbox,
    CTkToplevel,
    E,
    N,
    S,
    W,
    set_appearance_mode,
)
from PIL import Image, ImageTk
from playsound import playsound  # type: ignore
from pyttsx3 import Engine, init  # type: ignore
from pyvolume import custom  # type: ignore

# pylint: disable=pointless-string-statement
"""Seagull Scaring V2
By Gabriel Alonso-Holt.

Recommended/default settings: 2700 seconds (timer), 60 seconds (min time), 300 seconds (max time).

The days of having me run around scaring seagulls manually are over! 
With Seagull Scaring, you can just start the program, 
choose a time to scare seagulls for, and relax as the seagulls fly away when you want.

Instructions:

1. Start program ("python main.pyw" is preferred, it's your choice how to run it, not mine)
2. Input your settings or use default settings, then click "scare the gulls".
3. Every (minimum wait time - maximum wait time) minutes or seconds, you will hear a seagull squawk.
4. At least 1 seagull should fly away every time the noise is played.
5. When the program finishes, you will see finish time and approximate number of seagulls scared.

"""

seed()

# Load config file
parser: ConfigParser = ConfigParser()
parser.read(r"ssv2cfg.ini")

config: list[str] = parser.sections()

FMT: str = "%d.%m.%y %H:%M:%S"

# define a root element
root: CTk = CTk()
root.title(string="Seagull Scaring V2")
root.geometry(geometry_string="400x400+200+200")
root.resizable(width=False, height=False)
set_appearance_mode("light")


def get_time(function: Any):
    """

    Times any function

    """

    def wrapper(*args: tuple[Any, ...], **kwargs: dict[Any, Any]) -> Any:

        start_time: float = perf_counter()

        response: Any = function(*args, **kwargs)
        end_time: float = perf_counter()
        total_time: float = end_time - start_time

        print(f"Time taken: {total_time:.2f} seconds.")

        return response

    return wrapper


def get_values() -> None:
    """

    Obtains and stores values from setting entry boxes.

    """

    global timer, min_time, max_time, effect, gull  # pylint: disable=global-variable-undefined

    effect = sounds.get()

    match effect:
        case "seagull":
            gull = r"media\seagull.wav"

        case "sad seagull":
            gull = r"media\sad_seagull.wav"

        case "confused seagull":
            gull = r"media\confused_seagull.wav"

        case "angry seagull":
            gull = r"media\angry_seagull.wav"

        case "disgust seagull":
            gull = r"media\disgust_seagull.wav"

        case "alarm seagull":
            gull = r"media\alarm_seagull.wav"

        case "robot seagull":
            gull = r"media\robot_seagull.wav"

        case "Seagull 2":
            gull = r"media\Seagull_2.wav"

        case "sea gull":
            gull = r"media\sea_gull.wav"

        case _:
            pass

    try:

        timer = int(scaring_time.get())  # type: ignore

        min_time = int(x_time.get())  # type: ignore
        max_time = int(y_time.get())  # type: ignore

    # Use default settings
    except NameError:

        timer = int(parser[config[0]]["scaring_time"])

        min_time = int(parser[config[0]]["min_time"])
        max_time = int(parser[config[0]]["max_time"])

        gull = parser[config[0]]["default_sound"]

    scare_gulls()


def scare_loop(start_config: str = "False") -> None:
    """

    Seagull scaring loop with log window.

    """

    global timer, min_time, max_time, effect, gull  # pylint: disable=global-variable-undefined global-variable-not-assigned

    log_window: CTkToplevel = CTkToplevel()
    log_window.title(string="seagull log")
    log_window.geometry(geometry_string="300x300+400+200")
    log_window.attributes("-topmost", 1)  # type: ignore
    log_window.resizable(width=False, height=False)

    seagull_image: Image.Image = Image.open(  # pylint: disable=redefined-outer-name
        r"seagull.png"
    )

    # icon
    seagull_icon: ImageTk.PhotoImage = ImageTk.PhotoImage(seagull_image)
    root.iconphoto(False, seagull_icon)

    seagull_log: CTkTextbox = CTkTextbox(
        master=log_window, width=300, height=300, activate_scrollbars=True
    )
    seagull_log.grid(sticky=N + E + S + W)  # type: ignore

    scroll_bar: CTkScrollbar = CTkScrollbar(master=seagull_log)
    scroll_bar.grid(sticky=E)  # type: ignore

    seagull_log.configure(yscrollcommand=scroll_bar.set)  # type: ignore

    seagulls_scared: int = 0

    if start_config == "True":

        gull = parser[config[0]]["default_sound"]
        min_time = int(parser[config[0]]["min_time"])
        max_time = int(parser[config[0]]["max_time"])
        timer = int(parser[config[0]]["scaring_time"])

    else:

        timer = int(scaring_time.get())
        min_time = int(x_time.get())  # type: ignore
        max_time = int(y_time.get())  # type: ignore
        gull = rf"media\{sounds.get().replace(" ", "_")}.wav"

    # Scare seagulls in a loop until timer reaches 0
    while timer > 0:

        pause: int = randint(a=min_time, b=max_time)
        playsound(gull)  # pylint: disable=possibly-used-before-assignment
        seagull_log.insert(1.0, f"A seagull was scared on {datetime.now():{FMT}}.\n")  # type: ignore pylint: disable=line-too-long
        seagulls_scared += 1
        sleep(pause)
        timer -= pause

    seagull_log.configure(state=DISABLED)  # type: ignore

    # Show a message box when done.
    showinfo(
        title="Seagull Scaring",
        message=f"Done!\nFinish time: {datetime.now():{FMT}}.\nSeagulls scared: {seagulls_scared:,}",
    )

    # Save to file?
    save_confirmation: bool = askyesno(
        title="Seagull Scaring", message="Do you want to save your logs to a file?"
    )
    if save_confirmation:

        with open(file=r"ssv2_log.txt", mode="a", encoding="utf-8") as file:

            data: str = seagull_log.get(index1=1.0, index2=END)  # type: ignore
            file.write(data)


def scare_gulls() -> None:
    """Starts seagull scaring in a separate thread."""

    start_value: str = parser[config[0]]["autostart"]

    thread: Thread = Thread(target=scare_loop, args={"autostart": start_value})
    thread.start()


def set_volume(volume: float) -> None:
    """Sets volume according to slider value"""

    custom(percent=int(volume))


def about_program() -> None:
    """Shows about window."""

    root_2: CTkToplevel = CTkToplevel()
    root_2.title(string="about this program")
    root_2.geometry(geometry_string="300x175")
    root_2.attributes("-topmost", 1)  # type: ignore
    root_2.resizable(width=False, height=False)

    # icon
    seagull_icon: ImageTk.PhotoImage = ImageTk.PhotoImage(seagull)  # type: ignore
    root_2.iconphoto(False, seagull_icon)

    def github() -> None:
        """Self promo?"""

        open_new(r"github.com/Gabriel-H189/SeagullScaringV2")

    def extract_gull_effects() -> None:
        """Unzips a `media.zip` from the program directory."""

        file_path: str = r"media.zip"
        with ZipFile(file=file_path, mode="r") as zip_file:

            zip_file.extractall("media")

    about_label: CTkLabel = CTkLabel(
        master=root_2,
        text="Seagull Scaring V2\nBy Gabriel Alonso-Holt",
        font=("calibri", 16, "bold"),
    )
    about_label.pack(pady=5)  # type: ignore

    gh_button: CTkButton = CTkButton(
        master=root_2, text="go to Gabriel's github", command=github
    )
    gh_button.pack(pady=7)  # type: ignore

    gull_effects_label: CTkLabel = CTkLabel(
        master=root_2, text="got gull effects?", font=("calibri", 16, "bold")
    )
    gull_effects_label.pack(pady=5)  # type: ignore

    extract_button: CTkButton = CTkButton(
        master=root_2, text="extract gull effects", command=extract_gull_effects
    )
    extract_button.pack()  # type: ignore

    if __name__ == "__main__":

        root_2.mainloop()


def autostart() -> None:
    """Autostart function only available through config file."""

    a_window: CTkToplevel = CTkToplevel()
    a_window.title(string="Autostart")
    a_window.attributes("-topmost", 1)  # type: ignore
    a_window.resizable(height=False, width=False)

    text: CTkTextbox = CTkTextbox(
        master=a_window, font=("calibri", 14, "bold"), wrap=WORD
    )
    text.pack()  # type: ignore

    abort: CTkButton = CTkButton(
        master=a_window, text="abort seagull scaring", command=exit
    )
    abort.pack()  # type: ignore

    def start() -> None:

        text.insert(END, "Autostart in...")  # type: ignore

        for i in range(int(parser[config[0]]["autostart_delay"]), 0, -1):

            text.insert(END, f"{i}!\n")  # type: ignore
            sleep(1)

        scare_gulls()

    if __name__ == "__main__":

        start()


def send_announcement() -> None:
    """Sends a Seagull Wars public service announcement."""

    message = askstring("Send announcement", "Enter message: ")

    def _send_a() -> None:

        playsound(r"media\alarm_seagull.wav")

        engine: Engine = init()  # type: ignore
        engine.setProperty("rate", 140)  # type: ignore
        engine.say(f"This is a Seagull Wars public service announcement. {message}")  # type: ignore

        engine.runAndWait()  # type: ignore

        playsound(r"media\alarm_seagull.wav")

    thread: Thread = Thread(target=_send_a)
    thread.start()
    

def check_media_folder() -> None:
    """Verifies that sound effects are available."""
    
    if not isdir(r"media"):
        
        showwarning(title="No sound effects", message="No media folder present!")


seagull: Image.Image = Image.open(fp=r"seagull.png")
seagull_image: CTkImage = CTkImage(seagull)

si_label: CTkLabel = CTkLabel(master=root, text="", image=seagull_image)
si_label.pack()  # type: ignore

# Icon
icon: ImageTk.PhotoImage = ImageTk.PhotoImage(seagull)
root.iconphoto(True, icon)

ss_label: CTkLabel = CTkLabel(master=root, text="Seagull Scaring", font=("arial", 16))
ss_label.pack()  # type: ignore

ts_label: CTkLabel = CTkLabel(master=root, text="Timer in seconds: ")
ts_label.place(x=90, y=53)  # type: ignore

scaring_time: CTkEntry = CTkEntry(master=root)
scaring_time.place(x=80, y=77)  # type: ignore
scaring_time.insert(0, parser[config[0]]["scaring_time"])  # type: ignore

xt_label: CTkLabel = CTkLabel(master=root, text="Minimum time: ")
xt_label.place(x=90, y=105)  # type: ignore

x_time: CTkEntry = CTkEntry(master=root)
x_time.place(x=80, y=130)  # type: ignore
x_time.insert(0, parser[config[0]]["min_time"])  # type: ignore

mt_label: CTkLabel = CTkLabel(master=root, text="Maximum time: ")
mt_label.place(x=90, y=161)  # type: ignore

y_time: CTkEntry = CTkEntry(master=root)
y_time.place(x=80, y=188)  # type: ignore
y_time.insert(0, parser[config[0]]["max_time"])  # type: ignore

seagull_values: list[str] = [
    "seagull",
    "sad seagull",
    "angry seagull",
    "confused seagull",
    "disgust seagull",
    "alarm seagull",
    "robot seagull",
    "Seagull 2",
    "sea gull",
]

select_sound_label: CTkLabel = CTkLabel(master=root, text="Select your sound: ")
select_sound_label.place(x=250, y=53)  # type: ignore

sounds: CTkComboBox = CTkComboBox(master=root, values=seagull_values)
sounds.place(x=250, y=77)  # type: ignore
sounds.set(parser[config[0]]["default_sound"])

scare_button: CTkButton = CTkButton(
    master=root, text="scare the gulls", command=get_values
)
scare_button.place(x=80, y=250)  # type: ignore

send_button: CTkButton = CTkButton(
    master=root, text="send announcement", command=send_announcement
)
send_button.place(x=80, y=290)  # type: ignore

volume_label: CTkLabel = CTkLabel(master=root, text="Volume")
volume_label.place(x=265, y=110)  # type: ignore

slider: CTkSlider = CTkSlider(
    master=root, from_=0, to=100, orientation=VERTICAL, command=set_volume
)
slider.place(x=275, y=140)  # type: ignore
slider.set(int(parser[config[0]]["default_volume"]))  # type: ignore

about_button: CTkButton = CTkButton(
    master=root, text="about", width=10, command=about_program
)
about_button.place(x=265, y=350)  # type: ignore

if parser[config[0]]["autostart"] == "True":

    autostart()
    
check_media_folder()

# Start program
if __name__ == "__main__":

    root.mainloop()  # type: ignore
    sys_exit()
