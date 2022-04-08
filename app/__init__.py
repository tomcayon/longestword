"""
Graphic Module
"""

import tkinter as tk
import tkinter.ttk as ttk

DIM = W,H = 1024,600

PADDING = 5

def open_palette(name):
    palette = {}
    with open(name,"r") as file:
        for key,value in zip(["bright","grey","dark","accent-dark","accent-bright"],
                            list(file.readlines())):
            palette[key] = value[:-1]


TITLE = "Jeu cool"
AUTHORS = "Les hommes daufins"
COLOR_PALETTE = open_palette("palette.txt")


class AppWindow():
    def __init__(self):
        self.window = tk.Tk()
        self.init_window()

        self.window.mainloop()

    def init_window(self):
        win = self.window

        self.frame_header = ttk.Frame(win)
        self.frame_content = ttk.Frame(win)
        self.frame_footer = ttk.Frame(win)

        self.game_display = GameDisplay(self.frame_content)

        self.init_header()
        self.init_content()
        self.init_footer()

        self.frame_header.pack()
        self.frame_content.pack()
        self.frame_footer.pack()

    def init_header(self):
        head = self.frame_header

        self.frame_header_content = {

                "Title" : ttk.Label(head,text=TITLE),
                "Author" : ttk.Label(head,text=AUTHORS)

                }

        for i,element in enumerate(self.frame_header_content):
            self.frame_header_content [element].grid(
                    row = 0,
                    column = i,
                    padx = PADDING,
                    pady = PADDING)

    def init_content(self):
        self.game_display.init_components()

    def init_footer(self):
        pass

class GameDisplay():
    def __init__(self,parent):
        self.parent = parent

    def init_components(self):
        parent = self.parent

        self.letter_selector = ttk.Frame(parent)
        self.letter_entry = ttk.Frame(parent)
        self.solution_displayer = ttk.Frame(parent)

        self.init_entry()

        self.letter_selector.pack()
        self.letter_entry.pack()
        self.solution_displayer.pack()

    def init_entry(self):
        #self.enterred_text = tk.StringVar("Type something")

        self.letter_entry_field = ttk.Entry(self.letter_entry)
        self.letter_entry.pack()


if __name__ == "__main__":
    test = AppWindow()