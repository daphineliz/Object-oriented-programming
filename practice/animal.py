class Animal:
    def __init__(self, species, name, habit):
        self.species = species
        self.name = name
        self.habit = habit
        
class Mammal(Animal):
    def __init__(self,species, name, habit, fur_color, is_fed):
        super().__init__(species, name, habit)
        self.fur_color = fur_color
        self.is_fed = is_fed
        
#method to show mammal's current state
    def feed(self):
            if not self.is_fed:
             print(f"You have fed the {self.name}")
       
            else:
                self.is_fed =True
                print(f"You are feeding the {self.name} for the second time")
           
            
lion = Mammal("Cat", "Lion", "Fights", "Brown", False)
cow = Mammal("Cow", "Cow", "Eats grass", "Black and white", True)

lion.feed()

cow.feed()
        