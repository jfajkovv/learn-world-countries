# Load all necessary modules.
import tkinter as tk
import tk_helpers as tk_h
import turtle as tl

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

        # Quiz start button.
        self.start_bttn = tk.Button(
            master=self,
            text="Start",
            #command=
        ).pack(side=tk.LEFT)

        # Toggle fullscreen mode.
        self.fscreen_bttn = tk.Button(
            master=self,
            text="Fullscreen",
            command=lambda: tk_h.toggle_fscreen(master=root)
        ).pack(side=tk.LEFT)

        # View application info.
        self.about_bttn = tk.Button(
            master=self,
            text="About",
            #command=
        ).pack(side=tk.LEFT)

        # Exit app button.
        self.quit_bttn = tk.Button(
            master=self,
            text="Quit",
            command=root.destroy
        ).pack(side=tk.LEFT)


class SeparatorFrame(tk.Frame):
    """Additional space between controls and input."""

    def __init__(self, master):
        super().__init__()


class UserInput(tk.Frame):
    """User's entry field and information."""

    def __init__(self, master):
        super().__init__()

        # User entry prompt.
        self.answer_entry = tk.Entry(
            master=self,
            bd=3
        ).pack(side=tk.LEFT)

        # Input confirmation button.
        self.answer_bttn = tk.Button(
            master=self,
            text="Answer",
            #command=
        ).pack(side=tk.LEFT, padx=10)


class TlPool(tl.ScrolledCanvas):
    """Handy scrolled background container."""

    def __init__(self, master):
        super().__init__(master)


class MainApplication(tk.Frame):
    """Application core structure"""

    def __init__(self, master):
        super().__init__()

        # Construct GUI components.
        self.top_bar = TopBar(master=self)
        self.controls = Controls(master=self.top_bar)
        self.separator = SeparatorFrame(master=self.top_bar)
        self.input = UserInput(master=self.top_bar)
        self.canvas = TlPool(master=root)

        # Place GUI components onto main frame.
        self.top_bar.pack(expand=True, fill=tk.BOTH, side=tk.TOP)
        self.controls.pack(fill=tk.BOTH, side=tk.LEFT)
        self.separator.pack(expand=True, side=tk.LEFT)
        self.input.pack(expand=True, side=tk.LEFT)
        self.canvas.pack(expand=True, fill=tk.BOTH, side=tk.TOP)


if __name__ == "__main__":
    # Tkinter root application instance.
    root = tk.Tk()
    root.title(APP_TITLE)
    root.geometry(ROOT_WINDOW)
#    root.attributes("-fullscreen", True)
    MainApplication(master=root).pack(side=tk.TOP, expand=True, fill=tk.BOTH)
    root.mainloop()
