#the device class
class Device:
    #Device method
    def info(self):
        print(f"Device information")
        
#the computer class
class Computer(Device):
    #Computer method that overrides the device method
    def info(self):
        print(f"Computer information")

#the laptop class
class Laptop(Computer):
    #my laptop method that overrides the computer method
    def info(self):
        #super function which calls computer info method
        super().info()
        
        #super function which calls device info method
        Device.info(self)
        
        #this method to print laptop info
        print(f"Laptop information")
        
#my laptop object
laptop = Laptop()
laptop.info()
            