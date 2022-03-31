"""
Graphic Module
"""

import tkinter as tk

class AppWindow():
    def __init__(self):
        self.init_window()

    def init_window(self):
        self.window = tk.Tk()
        self.window.title("Longest Word")