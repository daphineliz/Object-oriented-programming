#PY
from abc import ABC, abstractmethod

#abstractmethod
class User(ABC):
        
    def __init__(self,username,password):
        self.username = username
        self.password = password
        
    @abstractmethod
    def login(self):
        pass
    
class AdminUser(User):
    def __init__(self,username,password):
        super().__init__(username,password)
        self.otp = '1234'
    
    def login(self):
        self.username = input('Enter your username: ')
        self.password = input('Enter your password: ')
    
        otp = input('Enter otp sent: ')
        if otp == self.otp:
            print(f"Logged in as Admin")
        else:
            print(f"Please log in again")


class Guest(User):
    def __init__(self,username,password):
        super(). __init__(username,password)
        
    def login(self):
        print(f"{self.username} is logged in as Guest")

Emma = AdminUser('Emmak','emma')
Emma.login()
            