def get_screen_geometry():
    """Returns active screen size as a list."""
    import tkinter
    root = tkinter.Tk()
    root.update_idletasks()
    root.attributes("-fullscreen", True)
    root.state("iconic")
    screen_geometry = root.winfo_geometry()
    screen_geometry = screen_geometry.split('+', 1)[0].split('x')
    root.destroy()
    return screen_geometry
