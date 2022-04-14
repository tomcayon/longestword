import os

PATH = os.getcwd() + "/sorted/"

class DicoCompressor() :
    MIN_LENGTH = 3
    MAX_LENGTH = 9
    def __init__(self):
        pass

    def dico_compressor(self,path,dico):
        try: #create dir if it doesnt exist to put sorted dico in there
            os.mkdir(path)
        except FileExistsError:
            pass

        mode = "w"
        words_files = {}
        for n in range(self.MIN_LENGTH,self.MAX_LENGTH+1,1):
            # fill words files objects dictionary
            try :
                words_files [n] = open(path + "%i.txt"%(n), mode)
                words_files [n].truncate(0)
            except:
                raise(FileExistsError,
                "error openning this file : %i.txt"%(n))


        self.word_list=dico.read().split("\n")

        for word in self.word_list:
            if 3<=len(word)<=9:
                words_files[len(word)].write(str(word+"\n"))
            else : pass

if __name__=="__main__":
    with open("dico.txt","r") as dico:
        DicoCompressor().dico_compressor(PATH,dico)