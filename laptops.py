#class 3
class Laptops:
    def __init__(self, name, RAM):
        self.name = name
        self.RAM = RAM
        
#create method to show
    def show(self):
        print("Name:", self.name)
        print("RAM:", self.RAM)
        
#Create an object for laptops class
lenovo = Laptops("Lenovo", "16GB")
dell = Laptops("DELL", "8GB")
        
#call the show method
lenovo.show()   
dell.show()