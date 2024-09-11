#class 2
class Fashionbrands:
    def __init__(self, name, style):
        self.name = name
        self.style = style
        
#create method to show
    def show(self):
        print("Name:", self.name)
        print("Style:", self.style)
        
#Create an object for fashionbrands class
versace = Fashionbrands("Versace", "Summer rush")
GUCCI = Fashionbrands("GUCCI", "Vintage")
        
#call the show method
versace.show()   
GUCCI.show()