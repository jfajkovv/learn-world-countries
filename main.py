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

# Tkinter master application instance.
root = tk.Tk()
root.title(APP_TITLE)
root.geometry(ROOT_WINDOW)
root.attributes("-fullscreen", True)  # Start in fullscreen mode.

# Control buttons section.
controls = tk.Frame(master=root)
controls.pack(fill=tk.BOTH, side=tk.LEFT)

fscreen_bttn = tk.Button(
    master=controls,
    text="Fullscreen",
    command=lambda: tk_h.toggle_fscreen(master=root)
)
fscreen_bttn.pack(fill=tk.BOTH, side=tk.TOP)

quit_bttn = tk.Button(master=controls, text="Quit", command=root.destroy)
quit_bttn.pack(fill=tk.BOTH, side=tk.TOP)

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
