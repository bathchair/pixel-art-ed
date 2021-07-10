from tkinter import *
import tkinter.colorchooser
from tkmacosx import Button
from PIL import ImageGrab
from datetime import datetime

class PixelArt:


    def __init__(self, root):
        self.root = root
        self.root.title("Pixel Art Editor")

        cell_length = 50
        grid_width = 20
        grid_height = 10
        control_height = cell_length
        self.chosen_color = None
        self.is_pen_selected = False
        self.is_eraser_selected = False

        self.drawing_grid = Canvas(self.root)
        self.drawing_grid.grid(column=0, row=0, sticky=(N,E,S,W))

        self.cells = []
        for i in range(grid_width):
            for j in range(grid_height):
                cell = Frame(self.drawing_grid, width=cell_length, height=cell_length, bg="white", highlightbackground="black", highlightcolor="black", highlightthickness=1)
                cell.grid(column=i, row=j)
                cell.bind('<Button-1>', self.tap_cell)
                self.cells.append(cell)

        control_frame = Frame(self.root, height=control_height, bg='gray')
        control_frame.grid(column=0, row=1, sticky=(N,E,S,W))

        new_button = Button(control_frame, text="New", fg='black', command=self.press_new_button)
        new_button.grid(column=0, row=0, columnspan=2, sticky=(N,E,S,W), padx=5, pady=5)

        save_button = Button(control_frame, text="Save", command=self.press_save_button)
        save_button.grid(column=2, row=0, columnspan=2, sticky=(N,E,S,W), padx=5, pady=5)

        draw_button = Button(control_frame, text="Draw", command=self.press_draw_button)
        draw_button.grid(column=8, row=0, columnspan=2, sticky=(N,E,S,W), padx=5, pady=5)

        erase_button = Button(control_frame, text="Erase", command=self.press_erase_button)
        erase_button.grid(column=10, row=0, columnspan=2, sticky=(N,E,S,W), padx=5, pady=5)

        self.selected_color_box = Frame(control_frame, borderwidth=2, relief="raised", bg='white')
        self.selected_color_box.grid(column=15, row=0, sticky=(N,E,S,W), padx=5, pady=8)

        pick_color_button = Button(control_frame, text="Pick color", command=self.press_pick_color_button)
        pick_color_button.grid(column=17, row=0, columnspan=3, sticky=(N,E,S,W), padx=5, pady=5)

        cols, rows = control_frame.grid_size()
        for col in range(cols):
            control_frame.columnconfigure(col, minsize=cell_length)
            control_frame.rowconfigure(0, minsize=cell_length)

        self.color_chooser = tkinter.colorchooser.Chooser(self.root)


    def tap_cell(self, event):
        print("Cell tapped")
        widget = event.widget
        index = self.cells.index(widget)
        selected_cell = self.cells[index]
        if self.is_eraser_selected:
            selected_cell["bg"] = "white"
        elif self.is_pen_selected and self.chosen_color != None:
            selected_cell["bg"] = self.chosen_color

    def press_new_button(self):
        print("New button pressed")
        for cell in self.cells:
            cell["bg"] = "white"
        self.selected_color_box["bg"] = "white"
        self.chosen_color = None
        self.is_pen_selected = False
        self.is_eraser_selected = False

    def press_save_button(self):
        print("Save button pressed")
        x = self.root.winfo_rootx() + self.drawing_grid.winfo_x()
        y = self.root.winfo_rooty() + self.drawing_grid.winfo_y() + 35
        width = x + 2000
        height = y + 1000
        image_name = datetime.now().strftime("gallery/%Y-%m-%d-%H-%M-%S") + ".png"
        _ = ImageGrab.grab(bbox=(x, y, width, height)).save(image_name)
        print("Saved as", image_name)

    def press_draw_button(self):
        print("Draw button pressed")
        self.is_pen_selected = True
        self.is_eraser_selected = False

    def press_erase_button(self):
        print("Erase button pressed")
        self.is_pen_selected = False
        self.is_eraser_selected = True

    def press_pick_color_button(self):
        print("Pick color button pressed")
        color_info = self.color_chooser.show()
        print(color_info)
        chosen = color_info[1]
        if chosen != None:
            self.chosen_color = chosen
            self.selected_color_box["bg"] = self.chosen_color


root = Tk()
PixelArt(root)
root.mainloop()