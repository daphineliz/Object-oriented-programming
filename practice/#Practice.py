#Practice
from abc import ABC, abstractmethod

#abstract anus
class Employee(ABC):
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
        
    @abstractmethod
    def calculate_bonus():
        pass
    
class Manager(Employee):
    def __init__(self, name, employee_id, salary):
        super().__init__(name, employee_id, salary)
        self.bonus = 0.15
        self.assignments = []
        
    def calculate_bonus(self):
        bonus = self.salary * self.bonus 
        print(f"{self.name} bonus is {bonus}")
    
    def add_assignments(self, assignment):
        self.assignments.append(assignment)
    
    def display_assignments(self):
        print(f"{self.name} assignments:")
        
        for assignment in self.assignments:
            print(f"{assignment}")
        

liaz = Manager('Liaz', 'ED001', 50000)
liaz.calculate_bonus()
liaz.add_assignments('Fire Osborne cause he is gay')
liaz.add_assignments('Fire Nehemiah cause he likes big bummed Men')
liaz.add_assignments('Fire Nehemiah cause he likes big bummed Men')
liaz.display_assignments()
        
    