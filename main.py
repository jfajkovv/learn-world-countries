# Load all necessary modules.
import tkinter as tk
import tk_helpers as tk_h
import turtle as tl
import pandas as pd
from random import choice

# Handy global constants.
COORDS_DATA_FILE = "./assets/world_countries_coords.csv"  # Countries coords data file.
APP_TITLE = "Learn World Countries"
ROOT_WINDOW = "1280x720"  # Reduce window to 720p after minimising.
# https://commons.wikimedia.org/wiki/File:BlankMap-World-large.png
WORLD_MAP_IMG = "./assets/BlankMap-World-large.gif"  # File exported to .GIF.
WORLD_MAP_WIDTH = 2800
WORLD_MAP_HEIGHT = 1400
# https://www.clipartmax.com/middle/m2i8d3H7N4N4N4K9_pin-2-google-maps-pin-png
PIN_ICON = "./assets/map-pin-icon.gif"  # File exported to .GIF.
PIN_VERTICAL_SHIFT = 15  # So it points sharply onto the given country.
INIT_COUNTRY = "Egypt"
PIN_INIT_COORDS = (145.0, 231.0)

coords_data = pd.read_csv(COORDS_DATA_FILE)  # Prepare data file via pandas.
all_countries = coords_data.country.to_list()
known_countries = []
unknown_countries = []
next_country = INIT_COUNTRY
next_country_coords = PIN_INIT_COORDS
known = 0
unknown = 0


def set_pin(pin, coords):
    """Move pin turtle into given position."""
    xcoor = coords[0]
    ycoor = coords[1] + PIN_VERTICAL_SHIFT
    t_pin.goto(xcoor, ycoor)


def init_pin(turtle):
    """Set map pin into starting position."""
    # Turtle pin starter code.
    turtle.penup()
    turtle.speed("fastest")
    turtle.goto(0, 1000)
    screen.addshape(PIN_ICON)
    turtle.shape(PIN_ICON)
    turtle.speed("slowest")
    turtle.showturtle()

    # Place pin into starter position.
    set_pin(pin=turtle, coords=PIN_INIT_COORDS)


def mark_good(coords):
    """Puts green dot in place of known country."""
    t_good = tl.RawTurtle(screen)
    t_good.hideturtle()
    t_good.penup()
    t_good.speed("fastest")
    t_good.turtlesize(0.3)
    t_good.shape("circle")
    t_good.color("green")
    t_good.goto(coords)
    t_good.showturtle()


def mark_wrong(coords):
    """Puts red dot in place of wrongly named country."""
    t_wrong = tl.RawTurtle(screen)
    t_wrong.hideturtle()
    t_wrong.turtlesize(0.3)
    t_wrong.shape("circle")
    t_wrong.color("red")
    t_wrong.speed("fastest")
    t_wrong.penup()
    t_wrong.goto(coords)
    t_wrong.showturtle()


def clear_entry_field():
    """Resets user input field."""
    answer_entry.delete(0, tk.END)


def check_answer(answer, correct):
    """Confronts player input w/ correct answer."""
    if answer == correct:
        return True


def draw_country(states_list, learned):
    """Randomly picks next country to guess."""
    drawn_country = choice(states_list)
    while drawn_country in learned:
        drawn_country = choice(states_list)
    return drawn_country


def fetch_country_coords(country_name, data):
    """Randomly picks next country to guess."""
    drawn_country_data = data[data.country == country_name]
    drawn_country_xcoor = drawn_country_data.xcoor
    drawn_country_ycoor = drawn_country_data.ycoor
    return (float(drawn_country_xcoor), float(drawn_country_ycoor))


def update_known_lbl():
    global known
    known += 1
    next_lbl = f"Known: {known}"
    known_lbl.config(text=next_lbl)


def update_unknown_lbl():
    global unknown
    unknown += 1
    next_lbl = f"Unknown: {unknown}"
    unknown_lbl.config(text=next_lbl)


def get_user_input():
    """Fetches player country answer."""
    user_input = answer_entry.get().title()
    clear_entry_field()

    global next_country
    global next_country_coords
    global known
    global unknown

    if user_input == next_country:
        mark_good(coords=next_country_coords)
        known_countries.append(next_country)
        update_known_lbl()
    else:
        if next_country not in unknown_countries:
            mark_wrong(coords=next_country_coords)
            unknown_countries.append(next_country)
            update_unknown_lbl()

    if not all_countries:
        answer_entry.config(state="disabled")
        answer_bttn.config(state="disabled")
        t_pin.hideturtle()
        print("info: countries list depleted.")
    else:
        next_country = draw_country(states_list=all_countries, learned=known_countries)
        all_countries.remove(next_country)
        next_country_coords = fetch_country_coords(country_name=next_country, data=coords_data)
        set_pin(pin=t_pin, coords=next_country_coords)


def start():
    init_pin(turtle=t_pin)
    answer_entry.config(state="normal")
    answer_bttn.config(state="normal")


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

start_bttn = tk.Button(master=controls_frm, text="Start", command=start)
start_bttn.pack(side=tk.LEFT)

fscreen_bttn = tk.Button(
    master=controls_frm,
    text="Fullscreen",
    command=lambda: tk_h.toggle_fscreen(master=root)
)
fscreen_bttn.pack(fill=tk.BOTH, side=tk.LEFT)

about_bttn = tk.Button(master=controls_frm, text="About")
about_bttn.pack(fill=tk.BOTH, side=tk.LEFT)

# Separator frame.
sep_frm = tk.Frame(master=top_bar_frm)
sep_frm.pack(expand=True, side=tk.LEFT)

# User input section.
input_frm = tk.Frame(master=top_bar_frm)
input_frm.pack(expand=True, side=tk.LEFT)

user_input = tk.StringVar()
answer_entry = tk.Entry(master=input_frm, textvariable=user_input, bd=3)
answer_entry.pack(side=tk.LEFT)
answer_entry.config(state="disabled")
answer_entry.focus_set()

root.bind("<Return>", (lambda event: get_user_input()))

answer_bttn = tk.Button(master=input_frm, text="Answer", command=get_user_input)
answer_bttn.pack(side=tk.LEFT, padx=10)
answer_bttn.config(state="disabled")

known_lbl = tk.Label(master=input_frm, text=f"Known: {known}")
known_lbl.pack(side=tk.LEFT, padx=10)

unknown_lbl = tk.Label(master=input_frm, text=f"Unknown: {unknown}")
unknown_lbl.pack(side=tk.LEFT, padx=10)


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
screen.onclick(tk_h.get_tl_mouse_click_coords)

t_pin = tl.RawTurtle(screen)
t_pin.hideturtle()

root.mainloop()  # Evoke program's core loop.
