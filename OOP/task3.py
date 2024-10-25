#parent class
class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type
#method to start vehicle
    def startVehicle(self):
        print(f"My {self.vehicle_type} is starting")
        
#inherits from vehicle class
class Car(Vehicle):
    def __init__(self, vehicle_type, number_of_doors):
        super().__init__(vehicle_type)
        self.number_of_doors = number_of_doors
        
#method to display info
    def display_info(self):
        super().startVehicle()
        print(f"Number of doors: {self.number_of_doors}")
        
#class inheriting from car class
class ElectricCar(Car):
    def __init__(self, vehicle_type, number_of_doors, battery_capacity ):
        super().__init__(vehicle_type, number_of_doors)
        self.battery_capacity = battery_capacity        
        
#method to show info
    def show_info(self):
        super().display_info()
        print(f"Battery Capacity: {self.battery_capacity}")
        
        
#creating object of electric car class
myElectriccar = ElectricCar("Tesla", 2, 100)
myElectriccar.show_info()