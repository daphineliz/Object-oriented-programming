#class 4
class Schools:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        
#create method to show
    def show(self):
        print("Name:", self.name)
        print("Location:", self.location)
        
#Create an object for schools class
school_name = Schools("International Window School", "Mbarara")
MHS = Schools("Maryhill High School", "Mbarara")
        
#call the show method
school_name.show()   
MHS.show()