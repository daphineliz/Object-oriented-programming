#parent class
class Appliance:
    def __init__(self, brand, power):
        self.brand = brand
        self.power = power
#method to display appliance information
    def display_info(self):
        print(f"Brand: {self.brand} \nPower: {self.power}")

#child class
class WashingMachine(Appliance):
    def __init__(self, brand, power, drum_size):
        super().__init__(brand, power)
        self.drum_size = drum_size

#method to show washing machine details
    def show_details(self):
        super().display_info()
        print(f"Drum size: {self.drum_size}")
        
#washing machine object
clikon = WashingMachine("Clikon", "4000Watts", "7kgs")
clikon.show_details()
