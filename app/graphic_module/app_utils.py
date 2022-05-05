import os

class AppStrings():
    def __init__(self,file,lang):
        self.language = lang
        self.string = eval(open(file,'r').read())

    def get(self,name):
        return self.string[name][self.language]

class AppColors():
    def __init__(self,file):
        self.palette = eval(open(file,'r').read())

    def get(self,name):
        return self.palette[name]
