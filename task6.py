class Animal:
    
    #method that displays animal soud
    def sound(self):
        print(f"Some generic animal sound")

   #child class 1
class Dog(Animal):
    #method to display dog sound
    def sound(self):
        print(f"Bark!")
  #child class 2
class Cat(Animal):
    #method to display cat sound
    def sound(self):
        print(f"Meow!")
        
    #function that accepts and animal object and calls its sound
def make_animal_sound(animal):
        animal.sound()
        
   #creating instances of dog and cat
dog = Dog()
cat = Cat()

make_animal_sound(dog)


make_animal_sound(cat)
