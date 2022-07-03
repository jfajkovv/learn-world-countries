# Modules import section.
import tkinter as tk
import tk_helpers as tk_h

# Handy global settings.

# This one fetches active screen resolution.
ACTIVE_SCREEN_SIZE = tk_h.get_screen_geometry()
#print(ACTIVE_SCREEN_SIZE)

# https://www.freepik.com/premium-vector/world-map-with-countries-borders-outline_20366547.htm
WORLD_MAP_IMG = "./assets/world-map-with-countries-borders-outline.png"


# Master application function.
def main():
    root_window = tk.Tk()  # Init main window.
    root_window.title("Learn World Countries")  # Title bar name.
    # Stretch up root window so it fills the entire screen.
    root_window.geometry(ACTIVE_SCREEN_SIZE)

    root_window.mainloop()  # Core loop. Keep program running until exit.


if __name__ == "__main__":
    main()
