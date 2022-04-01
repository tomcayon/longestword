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
        self.window.geometry("1024x600")


if __name__ == "__main__":
    test = AppWindow()