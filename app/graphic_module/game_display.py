"""
The Game frame contained in the app window
"""

from .app_constants import *

class GameDisplay():
    def __init__(self,game_core):
        self.game_core = game_core

    def init_components(self,parent):
    
        self.letter_selector = tk.Frame(parent)
        self.word_entry = tk.Frame(parent)
        self.solution_displayer = ttk.Frame(parent)

        self.init_selector()
        self.init_entry()
        self.init_solutions_displayer()

        self.letter_selector.pack()
        self.word_entry.pack()
        self.solution_displayer.pack()

    def init_selector(self):
        self.letters_displayer_frame = tk.Frame(self.letter_selector)
        
        self.selector_button_consonnent = ttk.Button(
                self.letter_selector,text=APP_STRINGS.get("add_consonnent"),command=self.add_consonnent)
        self.selector_button_vowel = ttk.Button(
                self.letter_selector,text=APP_STRINGS.get("add_vowel"),command=self.add_vowel)
        
        self.selector_button_consonnent.grid(column=0,row=0,padx=PAD)
        self.selector_button_vowel.grid(column=1,row=0,padx=PAD)
        self.letters_displayer_frame.grid(column=2,row=0,padx=PAD)
        
        self.init_letters_displayer()
        
    def init_entry(self):
        self.enterred_text = tk.StringVar()
        self.enterred_text.trace("w",self.letter_typed)

        self.word_entry.config()

        self.word_entry_label = ttk.Label(
                self.word_entry,
                text=APP_STRINGS.get("word_entry_label"))
        
        self.word_entry_field = ttk.Entry(
                self.word_entry,
                textvariable=self.enterred_text)
        
        self.word_entry_button= ttk.Button(
                self.word_entry,text=APP_STRINGS.get("word_entry_submit"),
                command=self.submit_word)
        
    def show_entry(self):
        self.word_entry_label.pack(pady=PAD)
        self.word_entry_field.pack(pady=PAD)
        self.word_entry_button.pack(pady=PAD)

    def init_solutions_displayer(self):
        self.solution_displayer_list = tk.StringVar()
        self.solution_displayer_label = ttk.Label(
                self.solution_displayer,
                text=APP_STRINGS.get("solutions_label"))
        self.solution_displayer_listbox = tk.Listbox(
                self.solution_displayer,
                listvariable=self.solution_displayer_list)
                
        self.solution_displayer_label.pack()
        self.solution_displayer_listbox.pack()
        
    def init_letters_displayer(self):
        self.letters_displayer_label = ttk.Label(
                self.letters_displayer_frame,
                text=APP_STRINGS.get("letters_displayer_label"))
        
        self.letters_displayer_label.grid(row=0,column=0)
        self.letter_displayer_list = []
                
    def update_letters_displayer(self,letters):
        letters = list(letters)
        self.letter_displayer_list = []
        for i,l in enumerate(letters):
            self.letter_displayer_list.append(
                    ttk.Label(
                            self.letters_displayer_frame,
                            text=l,
                            background=APP_COLOR.get("accent-dark"),
                            font=LETTER_CARDS_STYLE,
                            state=tk.constants.DISABLED)
                            )
            
            self.letter_displayer_list[-1].grid(row=0,column=1+i,padx=PAD)

    def submit_word(self):
        word = self.enterred_text.get()
        wl = len(word)
        if wl < self.game_core.get_min_lenght():
            messagebox.showerror(
                    "Action forbidden",
                    APP_STRINGS.get("enter_longer_word")+"\nMin lenght : %i"%(
                            self.game_core.get_min_lenght()))
            
        elif wl > self.game_core.get_max_lenght():
            messagebox.showerror(
                    "Action forbidden",
                    APP_STRINGS.get("enter_smaller_word")+"\nMax lenght : %i"%(
                            self.game_core.get_max_lenght()))
        elif not self.game_core.is_word_possible(word):
            messagebox.showerror(
                    "Action forbidden",
                    APP_STRINGS.get("word_not_possible"))
                    
            self.word_entry_field.delete(0,"end")
        else:
            self.game_core.submit_word(self.enterred_text.get(),self)
            
    def add_consonnent(self):
        self.game_core.add_consonnent(self)
    
    def add_vowel(self):
        self.game_core.add_vowel(self)
        
    def disable_consonnent_selection(self):
        self.disable_button(self.selector_button_consonnent) 
        
    def disable_vowel_selection(self):
        self.disable_button(self.selector_button_vowel)
        
    def disable_letter_selection(self):
        self.selector_button_consonnent.grid_forget()
        self.selector_button_vowel.grid_forget()
        #self.letter_selector.pack_forget()
    
    def letter_typed(self,__var,__index,__op):
        txt = list(self.enterred_text.get())
        for l in txt:
            if l not in self.game_core.get_letters():
                txt.remove(l)
        self.enterred_text.set("".join(txt))
    
    def disable_entry(self):
        self.disable_button(self.word_entry_button)
        self.word_entry_button.config(text=APP_STRINGS.get("word_entry_button_word_enterred"))
        self.word_entry_field.config(
                state=tk.constants.DISABLED,
                foreground=APP_COLOR.get("accent-light"),
                cursor="X_cursor")
        self.word_entry_label.config(
                text=APP_STRINGS.get("word_entry_label_word_enterred"))
                
    def disable_button(self,button):
        button.config(
                state=tk.constants.DISABLED,
                cursor="X_cursor")
                
    def display_solutions(self,list):
        for i,el in enumerate(list):
            self.solution_displayer_listbox.insert(i,el)
    
    def show_reset(self):
        tk.messagebox.showwarning("Warning",APP_STRINGS.get("reset_letters_warning"))
        
    def show_result_message(self,result_code,max_lenght):
        msg_key = ("best_word","good_word","wrong_word")[result_code]
        tk.Label(self.solution_displayer,text=APP_STRINGS.get(msg_key)).pack()