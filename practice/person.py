class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        
#child class inheriting from person
class Employee(Person):
    def __init__(self, name, age, gender, employee_id, department):
        super().__init__(name, age, gender)
        self.employee_id = employee_id
        self.department = department
        self. task = None
#method to assign task
    def assign_task(self, task):
        
        if self.task == task:
            print(f"Task, {self.task} is already assigned to {self.name} of IdNo {self.employee_id} in {self.department} department.")
        
        else:
            self.task = task
            print(f"Task, {self.task} has been assigned to {self.name} of IdNo {self.employee_id} in {self.department} department.")
        
        
#method to display employee info
    def display_employee_info(self):
        print(f"Employee name: {self.name}\n Department:{self.department}\n Task assigned: {self.task} ")

# creating employee objects

Tomlee = Employee("Tomlee", 30, "Male", "E001", "Finance")
Sonia = Employee("Sonia", 25, "Female", "E002", "Management")

Tomlee.assign_task("Prepare reports")
Sonia.assign_task("Balance the logs")

Tomlee.assign_task("Prepare reports")
Tomlee.display_employee_info()
Sonia.display_employee_info()
