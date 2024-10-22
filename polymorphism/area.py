class Shape:
    def __init__(self, type, sides):
        self.type = type
        self.sides = sides
    def area(self):
        print(f"{self.type}'s Area is")
        
class Square(Shape):
    def __init__(self, type, sides, length):
        super().__init__(type, sides)
        self.length = length
        
    def area(self):
        print(f"Area = {self.length ** 2}cm^2")
        
#create object
square = Square("Square",4, 2)
square.area()
        
class Rectangle(Shape):
    def __init__(self, type, sides, length, width):
        super().__init__(type, sides)
        self.length = length
        self.width = width
    
    def area(self):
        print(f"Area = {self.length * self.width}cm^2")
        
#create object
rectangle = Rectangle("rectangle", 4, 5 , 2)
rectangle.area()
