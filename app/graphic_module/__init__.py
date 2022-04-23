"""
Graphic Module
"""

import tkinter as tk
import tkinter.ttk as ttk

import os


DIM = W,H = 1024,600

PALETTE = "palette.txt"
STRINGS = "strings.txt"

HEADER_STYLE = ("Times New Roman",20)
PAD = 5

APP_STRINGS = AppStings("fr")
APP_COLOR = AppColors()

class AppStings():
    def __init__(self,lang):
        self.language = lang
        self.string = eval(open(STRINGS,'r').read())

    def get(self,name):
        return self.string[name][self.language]

class AppColors():
    def __init__(self):
        self.palette = eval(open(PALETTE,'r').read())

    def get(self,name):
        return self.palette[name]


class AppWindow():
    def __init__(self):
        self.window = tk.Tk()

        self.window.tk.call("source", os.getcwd()+"/themes/Azure-ttk-theme-main/"+"azure.tcl")
        self.window.tk.call("set_theme", "dark")

        self.init_window()

        self.window.mainloop()

    def init_window(self):
        win = self.window
        self.window.config(padx=PAD,pady=PAD)

        self.frame_header = ttk.Frame(win)
        self.frame_content = ttk.Frame(win)
        self.frame_footer = ttk.Frame(win)

        self.game_display = GameDisplay(self.frame_content)

        self.init_header()
        self.init_content()
        self.init_footer()

        self.frame_header.pack()
        self.frame_content.pack(anchor=tk.CENTER)
        self.frame_footer.pack()

    def init_header(self):
        head = self.frame_header

        #print(APP_COLOR.get("accent-light"))

        self.frame_header_content = {

                "title" : ttk.Label(head,text=APP_STRINGS.get("title"),foreground=APP_COLOR.get("accent-light")),
                "author" : ttk.Label(head,text=APP_STRINGS.get("author"))

                }

        for i,element in enumerate(self.frame_header_content):
            self.frame_header_content [element].config(font=(HEADER_STYLE))
            self.frame_header_content [element].grid(
                    row = 0,
                    column = i,
                    padx = PAD,
                    pady = PAD)

    def init_content(self):
        self.game_display.init_components()

    def init_footer(self):
        pass




class GameDisplay():
    def __init__(self,parent):
        self.parent = parent

    def init_components(self):
        parent = self.parent

        self.letter_selector = tk.Frame(parent)
        self.word_entry = tk.Frame(parent)
        self.solution_displayer = ttk.Frame(parent)

        self.init_selector()
        self.init_entry()
        self.intt_displayer()

        self.letter_selector.pack()
        self.word_entry.pack()
        self.solution_displayer.pack()

    def init_selector(self):
        pass

    def init_entry(self):
        self.enterred_text = tk.StringVar()

        self.word_entry.config()

        self.word_entry_label = ttk.Label(self.word_entry,text=APP_STRINGS.get("word_entry_label"))
        self.word_entry_field = ttk.Entry(
                self.word_entry,
                textvariable=self.enterred_text)
        self.word_entry_button= ttk.Button(self.word_entry,text=APP_STRINGS.get("word_entry_submit"),command=self.submit_word)

        self.word_entry_label.pack(pady=PAD)
        self.word_entry_field.pack(pady=PAD)
        self.word_entry_button.pack(pady=PAD)

    def init_dispalyer(self):
        pass

    def submit_word(self):
        print(self.enterred_text.get())



if __name__ == "__main__":
    test = AppWindow()