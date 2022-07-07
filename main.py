# Load all necessary modules.
import tkinter as tk
import tk_helpers as tk_h
import turtle as tl

# Handy global constants.
#COOR_DATA = "./assets/world_countries_coords.csv"  # Countries coords data file.
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


def clear_entry_field():
    """Resets user input field."""
    answer_entry.delete(0, tk.END)


def get_user_input():
    """Fetches player country answer."""
    print(answer_entry.get())
    clear_entry_field()


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

user_input = tk.StringVar(master=input_frm)
answer_entry = tk.Entry(master=input_frm, textvariable=user_input, bd=3)
answer_entry.pack(side=tk.LEFT)
answer_entry.focus_set()

answer_bttn = tk.Button(master=input_frm, text="Answer", command=get_user_input)
answer_bttn.pack(side=tk.LEFT, padx=10)

root.bind("<Return>", (lambda event: get_user_input()))

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

screen.addshape(PIN_ICON)
t_pin = tl.RawTurtle(screen, shape=PIN_ICON)
t_pin.hideturtle()
t_pin.penup()
t_pin.goto(-12.0,420.0)
t_pin.showturtle()

root.mainloop()  # Evoke program's core loop.
