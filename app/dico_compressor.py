class DicoCompressor() :
    def __init__(self,dico):
        pass

    def dico_compressor(self,dico):
        MODE = "w"
        words_files = {
                3:open("3.txt",MODE),
                4:open("4.txt",MODE),
                5:open("5.txt",MODE),
                6:open("6.txt",MODE),
                7:open("7.txt",MODE),
                8:open("8.txt",MODE),
                9:open("9.txt",MODE),

                      }

        self.word_list=dico.read().split("\n")

        for word in self.word_list:
            if 3<=len(word)<=9:
                words_files[len(word)].write(str(word+"\n"))
            else : pass

if __name__=="__main__":
    with open("dico.txt","r") as dico:
        DicoCompressor(dico).dico_compressor(dico)