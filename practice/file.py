from abc import ABC, abstractmethod

class File(ABC):
    
    @abstractmethod
    def open(self):
        pass
    
    @abstractmethod
    def process(self):
        pass
    
class Textfile(File):
    def __init__(self, fileName):
        self.fileName = fileName
        
    def open(self):
        print(f"You are opening text file '{self.fileName}'")
    def process(self):
        print(f"Text file '{self.fileName}' is being processed")

class Imagefile(File):
    def __init__(self, fileName):
        self.fileName = fileName
        
    def open(self):
        print(f"You are opening image file '{self.fileName}'")
    def process(self):
        print(f"Image file '{self.fileName}' is being processed")
        
textfile = Textfile("document.txt")
imagefile = Imagefile("photo.jpg")

textfile.open()
textfile.process()

imagefile.open()
imagefile.process()

    
        