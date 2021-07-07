from tkinter import *

class PixelArt:

    def __init__(self, root):
        self.root = root
        self.root.title("Pixel Art Editor")

root = Tk()
PixelArt(root)
root.mainloop()