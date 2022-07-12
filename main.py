# Load all necessary modules.
import tkinter as tk

# Handy global constants.
APP_TITLE = "Learn World Countries"
ROOT_WINDOW = "1280x720"  # reduce window to 720p after minimising


class TopBar(tk.Frame):
    """Top bar controls aggregator."""

    def __init__(self, master):
        super().__init__()


class MainApplication(tk.Frame):
    """Application core structure"""

    def __init__(self, master):
        super().__init__()

        # Construct GUI components.
        self.top_bar = TopBar(master=self)

        # Place GUI components onto main frame.
        self.top_bar.pack(fill=tk.BOTH, side=tk.TOP)


if __name__ == "__main__":
    # Tkinter root application instance.
    root = tk.Tk()
    root.title(APP_TITLE)
    root.geometry(ROOT_WINDOW)
#    root.attributes("-fullscreen", True)
    MainApplication(master=root).pack(side="top", fill="both", expand=True)
    root.mainloop()
