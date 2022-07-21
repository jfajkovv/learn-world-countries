# Load all necessary modules.
import tkinter as tk
import tk_helpers as tk_h
import turtle as tl
import pandas as pd
from random import choice

# Handy global constants.
APP_TITLE = "Learn World Countries"
ROOT_WINDOW = "1280x720"  # reduce window to 720p after minimising
# https://commons.wikimedia.org/wiki/File:BlankMap-World-large.png
WORLD_COUNTRIES_BLANK_IMG = "./assets/BlankMap-World-large.gif"
WORLD_COUNTRIES_NAMED_IMG = "./assets/NamedMap-World-large.gif"
WORLD_COUNTRIES_WIDTH = 2800
WORLD_COUNTRIES_HEIGHT = 1400
# https://www.clipartmax.com/middle/m2i8d3H7N4N4N4K9_pin-2-google-maps-pin-png
PIN_ICON = "./assets/map-pin-icon.gif"  # file exported to .gif
PIN_STARTING_POSITION = (-180.0,-120.0)
PIN_VERTICAL_SHIFT = 15  # so it points sharply onto the given country


class ControlsBar(tk.Frame):
    """Control buttons sub-frame."""

    def __init__(self, master, countries_map):
        super().__init__()

        self.master = master
        self.countries_map = countries_map

        # Quiz start button.
        self.start_bttn = tk.Button(
            master=self,
            text="Start",
            command=self.start_quiz
        )
        self.start_bttn.pack(side=tk.LEFT, expand=True, fill=tk.X)

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
        # Bind ENTER key w/ answer_entry.
        root.bind("<Return>", (lambda event: self.get_user_input()))

        # Entry confirmation button.
        self.answer_bttn = tk.Button(
            master=self,
            text="Answer",
            command=self.get_user_input
        )
        self.answer_bttn.pack(side=tk.LEFT, expand=True, fill=tk.X)

        self.block_input()

    def start_quiz(self):
        self.master.countries_map.set_up_blank()

        self.master.t_pin.showturtle()

        self.countries_map.indicate_on_map(
            country=self.master.data_handler.next_country,
            pin=self.master.t_pin
        )

        self.enable_input()

        self.start_bttn.config(state="disabled")

    def get_user_input(self):
        input_sv = self.answer_entry.get().title()
        self.clear_entry_field()

        country = self.master.data_handler.next_country
        self.master.data_handler.validate_answer(
            user_answer=input_sv,
            correct_answer=country
        )

        self.master.data_handler.fetch_next_country()
        country = self.master.data_handler.next_country
        self.master.countries_map.indicate_on_map(
            country=country,
            pin=self.master.t_pin
        )

    def clear_entry_field(self):
        self.answer_entry.delete(0, tk.END)

    def block_input(self):
        self.answer_entry.config(state="disabled")
        self.answer_bttn.config(state="disabled")

    def enable_input(self):
        self.answer_entry.config(state="normal")
        self.answer_bttn.config(state="normal")
        self.answer_entry.focus_set()


class StatusBar(tk.Frame):
    """Information and score sub-frame."""

    def __init__(self, master):
        super().__init__()

        self.master = master
        self.known = tk.IntVar().get()
        self.all = len(self.master.data_handler.all_countries)

        self.status_lbl_txt = f"{self.known} / {self.all}"
        self.status_lbl = tk.Label(master=self, text=self.status_lbl_txt)
        self.status_lbl.pack(side=tk.RIGHT)

    def inc_known(self):
        self.known += 1

    def update_status(self):
        new_value = f"{self.known} / {self.all}"
        self.status_lbl.config(text=new_value)


class ScrolledCanvas(tl.ScrolledCanvas):
    """Handy scrolled background container."""

    def __init__(self, master):
        super().__init__(master)


class ScreenMap(tl.TurtleScreen):
    """Background graphics and turtle aggregator."""

    def __init__(self, master, canvas):
        super().__init__(canvas)

        self.master = master
        self.t_world_countries = None

        # Determine screen dimensions.
        self.screensize(WORLD_COUNTRIES_WIDTH, WORLD_COUNTRIES_HEIGHT)

        self.addshape(WORLD_COUNTRIES_BLANK_IMG)  # load blank world map image
        self.addshape(WORLD_COUNTRIES_NAMED_IMG)  # load named world map image
        self.addshape(PIN_ICON)  # load pin image

        # Fetch and print mouse click coordinates.
        self.onclick(tk_h.get_tl_mouse_click_coords)

        self.set_up_named()

    def set_up_named(self):
        self.t_world_countries = tl.RawTurtle(
            self,
            shape=WORLD_COUNTRIES_NAMED_IMG
        )

    def set_up_blank(self):
        self.t_world_countries.shape(WORLD_COUNTRIES_BLANK_IMG)

    def indicate_on_map(self, country, pin):
        coords = self.master.data_handler.fetch_country_coords(
            country=country,
            data_frame=self.master.data_handler.coords_data
        )
        self.master.t_pin.set_pin(position=coords, shift=PIN_VERTICAL_SHIFT)


class TurtlePin(tl.RawTurtle):
    """Moving turtle country indicator."""

    def __init__(self, master):
        super().__init__(master)

        # Turtle pin setup.
        self.hideturtle()
        self.shape(PIN_ICON)
        self.speed("fastest")
        self.penup()
        self.set_pin(position=PIN_STARTING_POSITION, shift=PIN_VERTICAL_SHIFT)
        self.speed("slowest")

    def set_pin(self, position, shift):
        xcoor = position[0]
        ycoor = position[1] + shift
        self.goto(xcoor, ycoor)


class MarkGood(TurtlePin):
    """Known country marker."""

    def __init__(self, master):
        super().__init__(master)

        # Good answer marker setup.
        self.hideturtle()
        self.shape("circle")
        self.color("green")
        self.turtlesize(0.3)
        self.speed("fastest")
        self.penup()


class MarkWrong(TurtlePin):
    """Unknown country marker."""

    def __init__(self, master):
        super().__init__(master)

        # Wrong answer marker setup.
        self.hideturtle()
        self.shape("circle")
        self.color("red")
        self.turtlesize(0.3)
        self.speed("fastest")
        self.penup()


class DataHandler(object):
    """This component is responsible for juggling app data."""

    # Countries coords data file.
    COORDS_DATA_FILE = "./assets/world_countries_coords.csv"

    def __init__(self, master):
        self.master = master

        self.coords_data = pd.read_csv(DataHandler.COORDS_DATA_FILE)
        self.all_countries = self.coords_data.country.to_list()
        self.next_country = self.draw_country(countries=self.all_countries)

    # Randomly pick next country to learn.
    def draw_country(self, countries):
        drawn_country = choice(countries)
        return drawn_country

    # Fetch given country coords.
    def fetch_country_coords(self, country, data_frame):
        country_data = data_frame[data_frame.country == country]
        country_xcoor = country_data.xcoor
        country_ycoor = country_data.ycoor
        return (float(country_xcoor), float(country_ycoor))

    # Check if the user knows correct country name.
    def validate_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            print(True)
            new_marker = MarkGood(master=self.master.countries_map)
            new_marker_position = self.fetch_country_coords(
                country=self.next_country,
                data_frame=self.coords_data
            )
            new_marker.set_pin(position=new_marker_position, shift=0)
            new_marker.showturtle()
            self.master.status_bar.inc_known()
            self.master.status_bar.update_status()
        else:
            print(False)
            new_marker = MarkWrong(master=self.master.countries_map)
            new_marker_position = self.fetch_country_coords(
                country=self.next_country,
                data_frame=self.coords_data
            )
            new_marker.set_pin(position=new_marker_position, shift=0)
            new_marker.showturtle()

    def fetch_next_country(self):
        try:
            self.all_countries.remove(self.next_country)
            self.next_country = self.draw_country(countries=self.all_countries)
        except IndexError:
            self.master.controls_bar.block_input()
            self.master.t_pin.hideturtle()


class MainApplication(tk.Frame):
    """Application core structure."""

    def __init__(self, master):
        super().__init__()

        self.data_handler = DataHandler(master=self)

        # Construct GUI components.
        self.canvas = ScrolledCanvas(master=self)
        self.countries_map = ScreenMap(master=self, canvas=self.canvas)
        self.controls_bar = ControlsBar(
            master=self,
            countries_map=self.countries_map
        )
        self.status_bar = StatusBar(master=self)

        # Place GUI components onto main frame.
        self.controls_bar.pack(side=tk.TOP, fill=tk.X)
        self.canvas.pack(side=tk.TOP, expand=True, fill=tk.BOTH)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

        self.t_pin = TurtlePin(master=self.countries_map)


if __name__ == "__main__":
    # Tkinter root application instance.
    root = tk.Tk()
    root.title(APP_TITLE)
    root.geometry(ROOT_WINDOW)
#    root.attributes("-fullscreen", True)
    MainApplication(master=root).pack(side=tk.TOP, expand=True, fill=tk.BOTH)
    root.mainloop()
