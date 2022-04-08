class WordFinder() :

    def find_word(self,dico_path,letters):
        a=0
        MODE = "r"
        words_files = {
                3:open(dico_path+"3.txt",MODE),
                4:open(dico_path+"4.txt",MODE),
                5:open(dico_path+"5.txt",MODE),
                6:open(dico_path+"6.txt",MODE),
                7:open(dico_path+"7.txt",MODE),
                8:open(dico_path+"8.txt",MODE),
                9:open(dico_path+"9.txt",MODE),

                      }

        dissociate_letters=[]
        for l in letters:
            dissociate_letters.append(l)

        set_dissociate_letters=set(dissociate_letters)
        possible_words=[]
        order=[9,8,7,6,5,4,3]
        for number in order:
            for word in words_files[number].readlines():
                sliced_word=[]
                word = word[:-1]
                for l in word:
                    sliced_word.append(l)
                set_sliced_word=set(sliced_word)
                intersection=set_dissociate_letters.intersection(set_sliced_word)
                if len(intersection)==number:
                    possible_words.append(word)
        print(possible_words)
        for word in possible_words:
            if len(possible_words[0])!=len(word):
                remove(world)











if __name__=="__main__":
   WordFinder().find_word("dico_sorted/","mreach")
