# Load all necessary modules.
import tkinter as tk
import tk_helpers as tk_h
import turtle as tl
import pandas as pd
from random import choice

# Handy global constants.
COOR_DATA_FILE = "./assets/world_countries_coords.csv"  # Countries coords data file.
APP_TITLE = "Learn World Countries"
ROOT_WINDOW = "1280x720"  # Reduce window to 720p after minimising.

# Graphics.
# https://commons.wikimedia.org/wiki/File:BlankMap-World-large.png
WORLD_MAP_IMG = "./assets/BlankMap-World-large.gif"  # File exported to .GIF.
WORLD_MAP_WIDTH = 2800
WORLD_MAP_HEIGHT = 1400
# https://www.clipartmax.com/middle/m2i8d3H7N4N4N4K9_pin-2-google-maps-pin-png
PIN_ICON = "./assets/map-pin-icon.gif"  # File exported to .GIF.
PIN_VERTICAL_SHIFT = 15  # So it points sharply onto the map.
PIN_INIT_COORDS = (145.0, 231.0)
INIT_POS = True

coor_data = pd.read_csv(COOR_DATA_FILE)
all_countries = coor_data.country.to_list()
guessed_countries = []


def set_pin(pin, coords):
    """Move pin turtle into given position."""
    xcoor = coords[0]
    ycoor = coords[1] + PIN_VERTICAL_SHIFT
    t_pin.goto(xcoor, ycoor)


def init_pin(turtle):
    """Set map pin into starting position."""
    set_pin(pin=turtle, coords=PIN_INIT_COORDS)


def clear_entry_field():
    """Resets user input field."""
    answer_entry.delete(0, tk.END)


def check_answer(answer, correct):
    if global INIT_POS == True:
    if user_answer == correct_answer:
        print(True)
        # add score

    # randomly change pin position
    


def draw_country(states_list):
    """Randomly picks next country to guess."""
    next_country = choice(states_list)
    return next_country


def draw_country_coords(country_name, data):
    """Randomly picks next country to guess."""
    next_country_data = data[data.country == country_name]
    next_country_xcoor = next_country_data.xcoor
    next_country_ycoor = next_country_data.ycoor
    return (float(next_country_xcoor), float(next_country_ycoor))


def get_user_input():
    """Fetches player country answer."""
    answer = answer_entry.get().title()
    clear_entry_field()
    check_answer(answer=answer, correct=correct)
    next_country = draw_country(states_list=all_countries)
    next_coords = draw_country_coords(country_name=next_country, data=coor_data)
    set_pin(pin=t_pin, coords=next_coords)

# Tkinter master application instance.
root = tk.Tk()
root.title(APP_TITLE)
root.geometry(ROOT_WINDOW)
root.attributes("-fullscreen", True)  # Start in fullscreen mode.

top_bar_frm = tk.Frame(master=root)
top_bar_frm.pack(fill=tk.BOTH, side=tk.TOP)

# Control buttons section.
controls_frm = tk.Frame(master=top_bar_frm)
controls_frm.pack(fill=tk.BOTH, side=tk.LEFT)

fscreen_bttn = tk.Button(
    master=controls_frm,
    text="Fullscreen",
    command=lambda: tk_h.toggle_fscreen(master=root)
)
fscreen_bttn.pack(fill=tk.BOTH, side=tk.LEFT)

about_bttn = tk.Button(master=controls_frm, text="About")
about_bttn.pack(fill=tk.BOTH, side=tk.LEFT)

# User input section.
input_frm = tk.Frame(master=top_bar_frm)
input_frm.pack(expand=True, side=tk.LEFT)

user_input = tk.StringVar()
answer_entry = tk.Entry(master=input_frm, textvariable=user_input, bd=3)
answer_entry.pack(side=tk.LEFT)
answer_entry.focus_set()

root.bind("<Return>", (lambda event: get_user_input()))

answer_bttn = tk.Button(master=input_frm, text="Answer", command=get_user_input)
answer_bttn.pack(side=tk.LEFT, padx=10)

# Exit section.
exit_frm = tk.Frame(master=top_bar_frm)
exit_frm.pack(fill=tk.BOTH, side=tk.LEFT)

quit_bttn = tk.Button(master=exit_frm, text="Quit", command=root.destroy)
quit_bttn.pack(fill=tk.BOTH, side=tk.RIGHT)

# This instance is where all my turtles live and play.
canvas = tl.ScrolledCanvas(
    master=root
)
canvas.pack(expand=tk.YES, fill=tk.BOTH)  # Stack canvas into the app.

# Put turtle screen onto the canvas.
screen = tl.TurtleScreen(cv=canvas)
screen.screensize(WORLD_MAP_WIDTH, WORLD_MAP_HEIGHT)
screen.addshape(WORLD_MAP_IMG)  # Load map img into the program as a turtle shape.
t_world_map = tl.RawTurtle(screen, shape=WORLD_MAP_IMG)

# Get mouse click coordinates.
screen.onclick(tk_h.get_tl_mouse_click_coor)

t_pin = tl.RawTurtle(screen)
t_pin.speed("slowest")
t_pin.hideturtle()
t_pin.penup()
t_pin.goto(0, 1000)
screen.addshape(PIN_ICON)
t_pin.shape(PIN_ICON)
t_pin.showturtle()

init_pin(turtle=t_pin)

root.mainloop()  # Evoke program's core loop.
