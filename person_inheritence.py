class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    #method to display info
    def display_info(self):
        print(f'My name is {self.name} and I am {self.age} years old.')
        
# class student that inherits from person
class Student(Person):
    def __init__(self, name, age, accessNumber):
        super().__init__(name, age) #calls initializer from person class
        self.accessNumber = accessNumber
    
    #method to display student info
    def display_studentInfo(self):
        super().display_info() # calls display info from Person class
        print(f'Access Number: {self.accessNumber}')
        
    #create object
daphineliz = Student("Musiimenta Daphineliz", 21, "A98260" )

#print(daphineliz)
daphineliz.display_studentInfo()

#class staff
class Staff(Person):
    def __init__(self, name, age, staffId):
        super().__init__(name, age)
        self.staffId = staffId
        
    #method to display staff info
    def display_staffInfo(self):
        super().display_info()
        print(f'Staff ID: {self.staffId}')
        
    #create staff obaject
simon = Staff("Simon Muhumuza", 30, "S001")

simon.display_staffInfo()