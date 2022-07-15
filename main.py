# Load all necessary modules.
import tkinter as tk
import tk_helpers as tk_h
import turtle as tl

# Handy global constants.
APP_TITLE = "Learn World Countries"
ROOT_WINDOW = "1280x720"  # reduce window to 720p after minimising
# https://commons.wikimedia.org/wiki/File:BlankMap-World-large.png
WORLD_COUNTRIES_IMG = "./assets/BlankMap-World-large.gif"  # file exported to .gif
WORLD_COUNTRIES_WIDTH = 2800
WORLD_COUNTRIES_HEIGHT = 1400
# https://www.clipartmax.com/middle/m2i8d3H7N4N4N4K9_pin-2-google-maps-pin-png
PIN_ICON = "./assets/map-pin-icon.gif"  # file exported to .gif
PIN_STARTING_POSITION = (-180.0,-120.0)


class ControlsBar(tk.Frame):
    """Control buttons sub-frame."""

    def __init__(self, master):
        super().__init__()

        self.master = master

        # Quiz start button.
        self.start_bttn = tk.Button(
            master=self,
            text="Start",
            command=self.master.start_quiz
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
        self.answer_sv = tk.StringVar()
        self.answer_entry = tk.Entry(
            master=self,
            textvariable=self.answer_sv,
            bd=3
        )
        self.answer_entry.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=10)
        self.answer_entry.config(state="disabled")
        # Bind ENTER key w/ answer_entry.
        root.bind("<Return>", (lambda event: self.get_user_input()))

        # Entry confirmation button.
        self.answer_bttn = tk.Button(
            master=self,
            text="Answer",
            command=self.get_user_input
        ).pack(side=tk.LEFT, expand=True, fill=tk.X)

    def get_user_input(self):
        input_sv = self.answer_entry.get().title()
        self.clear_entry_field()
        print(input_sv)
#        return input_sv

    def clear_entry_field(self):
        self.answer_entry.delete(0, tk.END)


class ScrolledCanvas(tl.ScrolledCanvas):
    """Handy scrolled background container."""

    def __init__(self, master):
        super().__init__(master)


class Screen(tl.TurtleScreen):
    """Background graphics and turtle aggregator."""

    def __init__(self, canvas):
        super().__init__(canvas)

        # Determine screen dimensions.
        self.screensize(WORLD_COUNTRIES_WIDTH, WORLD_COUNTRIES_HEIGHT)

        self.addshape(WORLD_COUNTRIES_IMG)  # load world map image
        self.addshape(PIN_ICON)  # load pin image
        # Initialise a turtle and change it's shape into background graphics.
        t_world_countries = tl.RawTurtle(self, shape=WORLD_COUNTRIES_IMG)

        # Fetch and print mouse click coordinates.
        self.onclick(tk_h.get_tl_mouse_click_coords)


class TurtlePin(tl.RawTurtle):
    """Moving turtle country indicator."""

    def __init__(self, master):
        super().__init__(master)

        # Turtle pin setup.
        self.hideturtle()
        self.shape(PIN_ICON)
        self.speed("fastest")
        self.penup()
        self.set_pin(coords=PIN_STARTING_POSITION)
        self.speed("slowest")
        self.showturtle()

    def set_pin(self, coords):
        self.goto(coords)


class MainApplication(tk.Frame):
    """Application core structure"""

    def __init__(self, master):
        super().__init__()

        # Construct GUI components.
        self.controls_bar = ControlsBar(master=self)
        self.canvas = ScrolledCanvas(master=self)
        self.screen = Screen(canvas=self.canvas)

        # Place GUI components onto main frame.
        self.controls_bar.pack(side=tk.TOP, fill=tk.X)
        self.canvas.pack(side=tk.TOP, expand=True, fill=tk.BOTH)

        self.t_pin = None

    def start_quiz(self):
        self.t_pin = TurtlePin(master=self.screen)
        self.controls_bar.answer_entry.config(state="normal")
        self.controls_bar.answer_entry.focus_set()


if __name__ == "__main__":
    # Tkinter root application instance.
    root = tk.Tk()
    root.title(APP_TITLE)
    root.geometry(ROOT_WINDOW)
#    root.attributes("-fullscreen", True)
    MainApplication(master=root).pack(side=tk.TOP, expand=True, fill=tk.BOTH)
    root.mainloop()
