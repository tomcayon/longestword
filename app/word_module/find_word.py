class WordFinder() :
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
                raise(FileExistsError,
                "error openning this file : %i.txt"%(n))

        letters = set(letters.lower() )
        possible_words=[]
        order=list(range(self.MAX_LENGTH,self.MIN_LENGTH,-1))

        for n in order:

            for word in words_files[n].readlines():

                sliced_word = set(word[:-1])

                intersection=letters.intersection(sliced_word)
                if len(intersection)==n:
                    possible_words.append(word)

        for word in possible_words:
            if len(possible_words[0])!=len(word):
                remove(world)

if __name__=="__main__":
   WordFinder().find_word("../dico/","mreacheic")