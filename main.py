# Load all necessary modules.
import tkinter as tk

# Handy global constants.
APP_TITLE = "Learn World Countries"
ROOT_WINDOW = "1280x720"  # reduce window to 720p after minimising


class TopBar(tk.Frame):
    """Top bar controls aggregator."""

    def __init__(self, master):
        super().__init__()


class Controls(tk.Frame):
    """Control buttons sub-frame."""

    def __init__(self, master):
        super().__init__()

        self.start_bttn = tk.Button(
            master=self,
            text="Start",
            #command=
        ).pack(side=tk.LEFT)


class MainApplication(tk.Frame):
    """Application core structure"""

    def __init__(self, master):
        super().__init__()

        # Construct GUI components.
        self.top_bar = TopBar(master=self)
        self.controls = Controls(master=self.top_bar)

        # Place GUI components onto main frame.
        self.top_bar.pack(fill=tk.BOTH, side=tk.TOP)
        self.controls.pack(fill=tk.BOTH, side=tk.LEFT)


if __name__ == "__main__":
    # Tkinter root application instance.
    root = tk.Tk()
    root.title(APP_TITLE)
    root.geometry(ROOT_WINDOW)
#    root.attributes("-fullscreen", True)
    MainApplication(master=root).pack(side="top", fill="both", expand=True)
    root.mainloop()
