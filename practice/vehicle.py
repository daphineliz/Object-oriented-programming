class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        
#car class inheriting from vehicle
class Car(Vehicle):
    def __init__(self, make, model, year, fuel_type, tank_capacity):
        super().__init__(make, model, year)
        self.fuel_type = fuel_type
        self.tank_capacity = tank_capacity
        self. fuel_amount = 0
#method to add fuel
    def refuel(self, amount):
        if self.fuel_amount + amount > self.tank_capacity:
            print(f"Reduce fuel amount, its beyong car tank capacity")
            
        else:
            self.fuel_amount += amount
            print(f"Added fuel: {amount}\n Current fuel_amount:{self.fuel_amount}")
        
    #stimulate driving
    def drive(self, distance, fuelConsumption_perKm):
        required_fuel = distance * fuelConsumption_perKm
        if self.fuel_amount >= required_fuel:
            self.fuel_amount -= required_fuel
            print(f"Drove: {distance}km\nRemaining fuel_amount: {self.fuel_amount}")
            
        else:
            print(f"Not enough fuel to drive {distance}km. Please refuel")
            
    #method to display vehicle info
    def display_vehicle_info(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}, Fuel Type: {self.fuel_type}, Tank Capacity: {self.tank_capacity}, Fuel Amount: {self.fuel_amount}")
    
        
myCar = Car("Ford", "Wrangler", 2018, "Petrol", 100)

myCar.refuel(50)
myCar.drive(120, 0.5)

myCar.display_vehicle_info()