#class 5
class wines:
    def __init__(self, name, origin):
        self.name = name
        self.origin = origin
        
#create method to show
    def show(self):
        print("Name:", self.name)
        print("Origin:", self.origin)
        
#Create an object for wines class
fourcousins = wines("FourCousins", "South Africa")
JPchenet = wines("JP.Chenet", "France")
        
#call the show method
fourcousins.show()   
JPchenet.show()