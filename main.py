# Modules importing section.
#import turtle

# Handy global settings.
# https://www.freepik.com/premium-vector/world-map-with-countries-borders-outline_20366547.htm
#BACKGROUND_IMG = "world-map-with-countries-borders-outline.png"

#WINDOW_WIDTH = 800
#WINDOW_HEIGHT = 600

# Create main window instance.
#window = turtle.Screen()
# Providing floating point arguments (% of screen) forces window into
# full screen mode (1.0 == 100%).
#window.setup(WINDOW_WIDTH, WINDOW_HEIGHT)
#window.bgpic(BACKGROUND_IMG)

# Exit after clicking anywhere on the screen.
#window.mainloop()

###

#import tkinter

#root_window = tkinter.Tk()
#root_window.title("learn-world-countries")
#root_window.attributes("-fullscreen", True)

#BACKGROUND_IMG = tkinter.PhotoImage(file="world-map-with-countries-borders-outline.png")

#bg_canvas = tkinter.Canvas(root_window, yscrollcommand=True)
#bg_canvas.pack(fill="both", expand=True)
#bg_canvas.create_image(0, 0, image=BACKGROUND_IMG, anchor="nw")

#scrollbar = tkinter.Scrollbar(bg_canvas, orient="horizontal", command=bg_canvas.yview)
#scrollbar.pack()

#root_window.mainloop()

###

import tkinter

class ScrollableImage(tkinter.Frame):
    def __init__(self, master=None, **kw):
        self.image = kw.pop('image', None)
        sw = kw.pop('scrollbarwidth', 10)
        super(ScrollableImage, self).__init__(master=master, **kw)
        self.cnvs = tkinter.Canvas(self, highlightthickness=0, **kw)
        self.cnvs.create_image(0, 0, anchor='nw', image=self.image)
        # Vertical and Horizontal scrollbars
        self.v_scroll = tkinter.Scrollbar(self, orient='vertical', width=sw)
        self.h_scroll = tkinter.Scrollbar(self, orient='horizontal', width=sw)
        # Grid and configure weight.
        self.cnvs.grid(row=0, column=0,  sticky='nsew')
        self.h_scroll.grid(row=1, column=0, sticky='ew')
        self.v_scroll.grid(row=0, column=1, sticky='ns')
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        # Set the scrollbars to the canvas
        self.cnvs.config(xscrollcommand=self.h_scroll.set, 
                           yscrollcommand=self.v_scroll.set)
        # Set canvas view to the scrollbars
        self.v_scroll.config(command=self.cnvs.yview)
        self.h_scroll.config(command=self.cnvs.xview)
        # Assign the region to be scrolled 
        self.cnvs.config(scrollregion=self.cnvs.bbox('all'))
        self.cnvs.bind_class(self.cnvs, "<MouseWheel>", self.mouse_scroll)

    def mouse_scroll(self, evt):
        if evt.state == 0 :
            self.cnvs.yview_scroll(-1*(evt.delta), 'units') # For MacOS
            self.cnvs.yview_scroll(int(-1*(evt.delta/120)), 'units') # For windows
        if evt.state == 1:
            self.cnvs.xview_scroll(-1*(evt.delta), 'units') # For MacOS
            self.cnvs.xview_scroll(int(-1*(evt.delta/120)), 'units') # For windows

import tkinter as tk

root = tk.Tk()
root.title("learn-world-countries")
root.attributes("-fullscreen", True)

# PhotoImage from tkinter only supports:- PGM, PPM, GIF, PNG format.
# To use more formats use PIL ImageTk.PhotoImage
img = tk.PhotoImage(file="world-map-with-countries-borders-outline.png")

image_window = ScrollableImage(root, image=img, scrollbarwidth=60, 
                               width=800, height=600)
image_window.pack()

root.mainloop()
