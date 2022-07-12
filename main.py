# Load all necessary modules.
import tkinter as tk

# Handy global constants.
APP_TITLE = "Learn World Countries"
ROOT_WINDOW = "1280x720"  # Reduce window to 720p after minimising.


class MainApplication(tk.Frame):
    """Application core structure"""

    def __init__(self, master):
        super().__init__()


if __name__ == "__main__":
    root = tk.Tk()
    root.title(APP_TITLE)
    root.geometry(ROOT_WINDOW)
#    root.attributes("-fullscreen", True)
    MainApplication(master=root).pack(side="top", fill="both", expand=True)
    root.mainloop()
