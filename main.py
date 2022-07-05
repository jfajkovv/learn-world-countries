# Load all necessary modules.
import tkinter as tk
import tk_helpers as tk_h
import turtle as tl

# Handy global constants.
COOR_DATA = "./assets/world_countries_coords.csv"
# https://commons.wikimedia.org/wiki/File:BlankMap-World-large.png
WORLD_MAP_IMG = "./assets/BlankMap-World-large.gif"  # File exported to .GIF.
WORLD_MAP_WIDTH = 2800
WORLD_MAP_HEIGHT = 1400
ACTIVE_SCREEN_SIZE = tk_h.get_screen_geometry()

# Tkinter master application instance.
root = tk.Tk()
root.title("Learn World Countries")
#root.geometry(ACTIVE_SCREEN_SIZE)  # Fit app window to the user's monitor.
root.attributes("-fullscreen", True)  # Fullscreen mode.

# Control buttons section.
controls = tk.Frame(master=root)
controls.pack(fill=tk.BOTH, side=tk.LEFT)

fscreen_bttn = tk.Button(
    master=controls,
    text="Fullscreen",
    command=lambda: tk_h.toggle_fscreen(master=root)
)
fscreen_bttn.pack(fill=tk.BOTH, side=tk.TOP)

quit_bttn = tk.Button(controls, text="Quit", command=root.destroy)
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
#screen.onclick(tk_h.get_mouse_click_coor)

root.mainloop()  # Evoke program's core loop.
