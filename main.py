# Load all necessary modules.
import tkinter as tk
import tk_helpers as tk_h
import turtle as tl

# Handy global constants.
APP_TITLE = "Learn World Countries"
ROOT_WINDOW = "1280x720"  # reduce window to 720p after minimising
WORLD_COUNTRIES_IMG = "./assets/BlankMap-World-large.gif"
WORLD_COUNTRIES_WIDTH = 2800
WORLD_COUNTRIES_HEIGHT = 1400


class ControlsBar(tk.Frame):
    """Control buttons sub-frame."""

    def __init__(self, master):
        super().__init__()

        # Quiz start button.
        self.start_bttn = tk.Button(
            master=self,
            text="Start",
            #command=
        ).pack(side=tk.LEFT, expand=True, fill=tk.X)

        # Toggle fullscreen mode button.
        self.fscreen_bttn = tk.Button(
            master=self,
            text="Fullscreen",
            command=lambda: tk_h.toggle_fscreen(master=root)
        ).pack(side=tk.LEFT, expand=True, fill=tk.X)

        # View application info button.
        self.about_bttn = tk.Button(
            master=self,
            text="About",
            #command=
        ).pack(side=tk.LEFT, expand=True, fill=tk.X)

        # Exit app button.
        self.quit_bttn = tk.Button(
            master=self,
            text="Quit",
            command=root.destroy
        ).pack(side=tk.LEFT, expand=True, fill=tk.X)

        # User entry prompt.
        self.answer_entry = tk.Entry(
            master=self,
            bd=3
        ).pack(side=tk.LEFT, expand=True, fill=tk.X, padx=10)

        # Entry confirmation button.
        self.answer_bttn = tk.Button(
            master=self,
            text="Answer",
            #command
        ).pack(side=tk.LEFT, expand=True, fill=tk.X)


class ScrolledCanvas(tl.ScrolledCanvas):
    """Handy scrolled background container."""

    def __init__(self, master):
        super().__init__(master)


class Screen(tl.TurtleScreen):
    """Background graphics and turtle aggregator."""

    def __init__(self, cv):
        super().__init__(cv)

        self.screensize(WORLD_COUNTRIES_WIDTH, WORLD_COUNTRIES_HEIGHT)
        self.addshape(WORLD_COUNTRIES_IMG)
        t_world_countries = tl.RawTurtle(self, shape=WORLD_COUNTRIES_IMG)
        # Get and print mouse click coordinates.
        self.onclick(tk_h.get_tl_mouse_click_coords)


class MainApplication(tk.Frame):
    """Application core structure"""

    def __init__(self, master):
        super().__init__()

        # Construct GUI components.
        self.controls_bar = ControlsBar(master=self)
        self.canvas = ScrolledCanvas(master=self)
        self.screen = Screen(cv=self.canvas)

        # Place GUI components onto main frame.
        self.controls_bar.pack(side=tk.TOP, fill=tk.X)
        self.canvas.pack(side=tk.TOP, expand=True, fill=tk.BOTH)


if __name__ == "__main__":
    # Tkinter root application instance.
    root = tk.Tk()
    root.title(APP_TITLE)
    root.geometry(ROOT_WINDOW)
#    root.attributes("-fullscreen", True)
    MainApplication(master=root).pack(side=tk.TOP, expand=True, fill=tk.BOTH)
    root.mainloop()
