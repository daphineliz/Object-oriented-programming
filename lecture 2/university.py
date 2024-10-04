class University:
    def __init__(self, name, location, slogan,branches = 1,):
        self.name = name
        self.location = location 
        self.slogan = slogan
        self.branches = branches
        
    def __str__(self) :
         return(f"University name: {self.name} Location: {self.location} Slogan: {self.slogan} Branches: {self.branches}")
         
         # create object
university1 = University("Uganda Christian University", "Mukono", "Center of Excellence", 3)
university2 = University("Kyambogo University", "Banda", "Pearl of Africa")
university3 = University("Victoria University", "Kampala", "Academic Excellence", 2)

print(university1)  
print(university2)    
print(university3)          