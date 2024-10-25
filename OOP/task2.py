#parent class 1
class Camera:
#My method to take photo
    def take_photo(selfcls):
        print(f"Taking a photo...")
        
#parent class 2
class Phone:
#My method to make a phone call
    def make_call(self):
        print(f"Making a phone call...")
        
#child class
class Smartphone(Camera, Phone):
    pass

#create smartphone object

smartphone = Smartphone()
smartphone.take_photo()
smartphone.make_call()