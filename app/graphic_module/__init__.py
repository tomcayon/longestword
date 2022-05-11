"""
Graphic Module
"""

#import the constants AND the libraries as tk and os
# the .[module_name] is because this is a file contained in this package
from .app_constants import *
from .game_display import GameDisplay

class AppWindow():
    def __init__(self,game_core):
        self.window = tk.Tk()
        self.window.geometry("%ix%i"%(W,H))
        self.game_display = GameDisplay(game_core)

        self.window.tk.call("source", PACKAGE_PATH+"/themes/Azure-ttk-theme-main/"+"azure.tcl")
        self.window.tk.call("set_theme", "dark")

        self.init_window()

    def start(self):
        self.window.mainloop()

    def init_window(self):
        win = self.window
        self.window.config(padx=PAD,pady=PAD)
        self.window.title(APP_STRINGS.get("win_title"))

        self.frame_header = ttk.Frame(win)
        self.frame_content = ttk.Frame(win)
        self.frame_footer = ttk.Frame(win)

        self.init_header()
        self.init_content()
        self.init_footer()

        self.frame_header.pack()
        self.frame_content.pack(anchor=tk.CENTER)
        self.frame_footer.pack()

    def init_header(self):
        head = self.frame_header

        self.header_logo_img=tk.PhotoImage(file=os.path.join(IMAGES_PATH,"logo_game.gif"))
        self.header_logo = tk.Label(self.frame_header,image=self.header_logo_img)
        self.header_logo.pack()

        self.rules_message = tk.Message(head,text=APP_STRINGS.get("instructions"),justify=tk.CENTER)
        self.rules_message.pack(pady=PAD)



    def init_content(self):
        self.game_display.init_components(self.frame_content)

    def init_footer(self):
        print(os.path.join(IMAGES_PATH,"logo_dolfin.png"))
        self.footer_logo_img=tk.PhotoImage(file=os.path.join(IMAGES_PATH,"logo_dolfin.png"))
        self.footer_logo = tk.Label(self.frame_footer,
                image=self.footer_logo_img,
                text=APP_STRINGS.get("author"),
                compound="left",
                font = HEADER_STYLE)
        self.footer_logo.pack()
