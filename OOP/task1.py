#Parent class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

#method to display device info
    def show_info(self):
        print(f"Device brand: {self.brand} \nDevice model: {self.model}")

#child class
class Smartphone(Device):
    def __init__(self, brand, model, storage_capacity):
        super().__init__(brand, model)
        self.storage_capacity = storage_capacity

#method to display smartphone info
    def show_info(self):
        super().show_info()
        print(f"Storage capacity: {self.storage_capacity}Gbs")
        
#create object of smartphone class
samsung = Smartphone("Samsung", "S24", 500)
samsung.show_info()