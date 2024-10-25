#parent class
class Employee:
    #method to display what the employee is doing
    def work(self):
        print(f"Employee is working")
        
#child class
class Manager(Employee):
    #method to dislay manager info
    def work(self):
        print(f"Manager is managing the team")
        
#child class
class Developer(Employee):
    #method to display developer info
    def work(self):
        print(f"Developer is writing code")
        
#manager object
manager = Manager()
manager.work()

#developer object
developer = Developer()
developer.work()
    