# Modules import section.
import tkinter as tk
import tk_helpers as tk_h

# Handy global settings.

# This one fetches active screen resolution and returns it as a list.
# First indice is width, second -- height.
ACTIVE_SCREEN_SIZE = tk_h.get_screen_geometry()
#print(ACTIVE_SCREEN_SIZE)
#WINDOW_WIDTH = ACTIVE_SCREEN_SIZE[0]
#WINDOW_HEIGHT = ACTIVE_SCREEN_SIZE[1]

# https://www.freepik.com/premium-vector/world-map-with-countries-borders-outline_20366547.htm
WORLD_MAP_IMG = "world-map-with-countries-borders-outline.png"


class Controls(tk.Frame):
    """Simple control pane."""

    def __init__(self, master):
        super().__init__()
        self.master = master

        self.button = tk.Button(master, text="this")
        self.button.pack()
        self.button = tk.Button(master, text="that")
        self.button.pack()

class MainAppGUI(tk.Frame):
    """General GUI aggregator class."""

    def __init__(self, master):
        super().__init__()
        self.master = master
        master.title("Learn World Countries")

        self.control_pane = Controls(master=self.master)


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry(ACTIVE_SCREEN_SIZE)
    MainAppGUI(master=root).pack()
    root.mainloop()
