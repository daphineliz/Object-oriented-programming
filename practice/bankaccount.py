class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.__account_number = account_number
        self.__initial_balance = initial_balance
        
        # Getter method for getting balance
    def get_balance(self):
        print(f"{self.__initial_balance}")
        
    # Method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__initial_balance += amount
            print(f"You have deposited {amount} on account number {self.__account_number}")
        else:
            print(f"Invalid deposit, Try again with valid amount")
            
    #method to withdraw
    def withdraw(self, amount):
        if amount >0 and amount <= self.__initial.balance:
            self.__initial_balance -= amount
            print(f"You have witdrawn {amount} and your new balance is {self.__initial_balance}")
        else:
            print(f"You have insufficient funds")
            
#objects

account1 = BankAccount("101", 20000)
account2 = BankAccount("102", 50000)


account1.deposit(10000)
account2.deposit(10000)
account1.get_balance()
account2.get_balance()
