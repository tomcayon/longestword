"""

Game engine Class
to manage everthing related to the gameplay

"""

import random
import word_module
from word_module.multiset import Multiset
import os

class GameEngine():
    
    MIN_LENGTH = 3
    MAX_LENGTH = 9
    
    MIN_VOWEL_CNT = 2
    
    CONSONNENTS = "zrtpqsdfghjklmwxcvbn"
    VOWEL = "aeyuio"
    
    ALLOWED_LETTERS = CONSONNENTS+VOWEL
    
    def __init__(self):
        self.letters = Multiset()
        
        self.consonnent_cnt = 0
        
    def submit_word(self,word,game_display):
        self.enterred_word = word
        game_display.disable_entry()
        game_display.display_solutions(word_module.WordsFinder().find_word(
                os.getcwd()+"/dico/",self.letters))
        
    def add_consonnent(self,game_display):
        if self.consonnent_cnt < self.MAX_LENGTH - self.MIN_VOWEL_CNT:
            self.add_letter(self.CONSONNENTS,game_display)
            self.consonnent_cnt += 1
        else:
            game_display.disable_consonnent_selection()
        
    def add_vowel(self,game_display):
        self.add_letter(self.VOWEL,game_display)
    
    def add_letter(self,letter_type,game_display):
        self.letters.add(random.choice(letter_type))
        game_display.update_letters_displayer(self.letters)
        
        if len(self.letters) >= self.MAX_LENGTH:
            game_display.disable_letter_selection()
            game_display.show_entry()
            
        print(self.letters)
        
    def get_min_lenght(self):
        return self.MIN_LENGTH
        
    def get_max_lenght(self):
        return self.MAX_LENGTH
    
    def get_letters(self):
        return self.ALLOWED_LETTERS
        
    def is_word_possible(self,word):
        return True
