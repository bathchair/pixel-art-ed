from tkinter import *

class PixelArt:

    def __init__(self, root):
        self.root = root
        self.root.title("Pixel Art Editor")

        cell_length = 50
        grid_width = 20
        grid_height = 10

        self.drawing_grid = Canvas(self.root)
        self.drawing_grid.grid(column=0, row=0, sticky=(N,E,S,W))

        self.cells = []
        for i in range(grid_width):
            for j in range(grid_height):
                cell = Frame(self.drawing_grid, width=cell_length, height=cell_length, bg="white", highlightbackground="black", highlightcolor="black", highlightthickness=1)
                cell.grid(column=i, row=j)
                self.cells.append(cell)



root = Tk()
PixelArt(root)
root.mainloop()