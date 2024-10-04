import random 

class Die:
    
    def __init__(self):
        self.sides = 6
        self.current_value = None
    
    #rolling the die
    def roll(self):
        self.current_value = random.randint(1, self.sides)
        return self.current_value
    
    #getting current value of the die
    def get_value(self):
        if self.current_value is None:
            return "Die hasnt been rolled yet"
        return self.current_value
    
    #resetting the die to none
    def reset(self):
        self.current_value = None
        
        
die = Die()
#roll the die and get a result

result = die.roll()
print(f"You rolled a {result}")

#getting current value without rolling again


print(f"Current value: {die.get_value()}")
# Reset the die's value
die.reset()
print(f"After reset: {die.get_value()}")
