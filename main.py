# Loading all necessary modules.
import turtle as tl

# Handy global constants.
# https://www.freepik.com/premium-vector/world-map-with-countries-borders-outline_20366547.htm
WORLD_MAP_IMG = "./assets/world-map-with-countries-borders-outline.gif"

screen = tl.Screen()
screenTk = screen.getcanvas().winfo_toplevel()
screenTk.attributes("-fullscreen", True)
screen.title("Learn World Countries")
screen.addshape(WORLD_MAP_IMG)
tl.shape(WORLD_MAP_IMG)

screen.mainloop()
