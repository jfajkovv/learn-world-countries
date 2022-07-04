def get_screen_geometry():
    """Returns active screen resolution."""
    import tkinter as tk
    root = tk.Tk()
    root.update_idletasks()
    root.attributes("-fullscreen", True)
    root.state("iconic")
    screen_geometry = root.winfo_geometry()
#    screen_geometry = screen_geometry.split('+', 1)[0].split('x')
    screen_geometry = screen_geometry.split('+', 1)[0]
    root.destroy()
    return screen_geometry
