# My dogs name and breed
class Dog:
    
    birthday = "01/03/2015"
    def __init__(self, name, breed, gender):
        self.name = name
        self.breed = breed
        self.gender = gender
     #method for bark   
    def bark(self):
        print("Wooffff Wooffff Wooffff Wooffff Wooffff ")
        
        #method to play
    def play(self):
        print("The dog is playing")
        
    #method to display 
    def display(self):
        print(f"My dog's name is {self.name} and the breed is a {self.breed}")
        print(f"Gender: {self.gender}")
        print(f"Birthday: {self.birthday}")
    
myDog = Dog("Maxine", "Ugandan Sheperd", "female")
myDog.display()

Bingo = Dog("Bingo", "Huskie", "Male")
Bingo.display()
Bingo.bark()
Bingo.play()



#My Dogs family tree
    
    