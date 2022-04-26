if __name__ == "__main__":
    from multiset import Multiset
else :
    from .multiset import Multiset

class WordsFinder() :
    MIN_LENGTH = 3
    MAX_LENGTH = 9

    def find_word(self,dico_path,letters):

        mode = "r"
        words_files = {}
        for n in range(self.MIN_LENGTH,self.MAX_LENGTH+1,1):
            # fill words files objects dictionary
            try :
                words_files [n] = open(dico_path + "%i.txt"%(n), mode)
            except:
                raise

        letters = Multiset(letters)
        possible_words=[]
        order=list(range(self.MAX_LENGTH,self.MIN_LENGTH,-1))

        for n in order:

            for word in words_files[n].readlines():

                sliced_word = Multiset(word[:-1])

                if sliced_word.issubset(letters):
                    possible_words.append(word[:-1])

        # for word in possible_words:
        #     if len(possible_words[0])!=len(word):
        #         remove(world)
        
        return possible_words
        
class WordChecker():
    def __init__(self,letters):
        self.letters = letters
        
    def is_word_possible(self,word):
        word = Multiset(word)
        letters = Multiset(self.letters)
        
        return word.issubset(letters)

if __name__=="__main__":
   print(WordsFinder().find_word("../dico/","cohmnaryt"))
