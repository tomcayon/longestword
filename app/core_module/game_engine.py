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
        
        game_display.disable_entry()
        game_display.display_solutions(self.solutions)
        
        if len(word)==len(self.solutions[0]) and word in self.solutions:
            result_code = 0 #best word
        elif word in self.solutions:
            result_code = 1 #good word
        else :
            result_code = 2 #wrong word
            
        game_display.show_result_message(result_code,self.solutions[0])
        
    def add_consonnent(self,game_display):
        self.add_letter(self.CONSONNENTS,game_display)
        self.consonnent_cnt += 1
        if self.consonnent_cnt > self.MAX_LENGTH - self.MIN_VOWEL_CNT:
            game_display.disable_consonnent_selection()
        
    def add_vowel(self,game_display):
        self.add_letter(self.VOWEL,game_display)
    
    def add_letter(self,letter_type,game_display):
        if len(self.letters)<self.MAX_LENGTH:
            self.letters.add(random.choice(letter_type))
            game_display.update_letters_displayer(self.letters)
        if len(self.letters) == self.MAX_LENGTH:
            self.solutions = word_module.WordsFinder().find_word(
                os.getcwd()+"/dico/",self.letters)
            if len(self.solutions)==0:
                self.letters = Multiset()
                game_display.update_letter_selection(self.letters)
                game_display.show_reset()
            else :
                game_display.disable_letter_selection()
                game_display.show_entry()
        
    def get_min_lenght(self):
        return self.MIN_LENGTH
        
    def get_max_lenght(self):
        return self.MAX_LENGTH
    
    def get_letters(self):
        return self.ALLOWED_LETTERS
        
    def is_word_possible(self,word):
        return word_module.WordChecker(self.letters).is_word_possible(word)
