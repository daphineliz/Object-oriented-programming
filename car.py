#Class 1

class Car:
    def __init__(self, model, price):
        self.model = model
        self.price = price
        
# creating method to display
    def display(self):
        print("Model:", self.model)
        print("Price:", self.price)

#Create an object for car class
ford = Car("Ford", 100)
toyota = Car("Toyota", 200)

#call the display method
ford.display()    
toyota.display()
    
 




