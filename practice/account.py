class BankAccount:
    def __init__(self, account_number, balance, account_holder):
        self.account_number = account_number
        self.balance = balance
        self.account_holder = account_holder
        
class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance, account_holder, interest_rate):
        super().__init__(account_number, balance, account_holder)
        self.interest_rate = interest_rate
        
    #method to deposit
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"You have deposited {amount} and your new balance is {self.balance}")
            
        else:
            print(f"Invalid deposit amount, Please try again")
            
    #method to withdraw
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"You have withdrawn {amount} and your new balance is {self.balance}")
            
        else:
            print(f"Insufficeint funds, Please try again later")
            
            
    #method to display account info
    def display_account_info(self):
        print(f"Account number: {self.account_number}\nCurrent balance: {self.balance}\nAccount holder: {self.account_holder}\nInterest rate: {self.interest_rate}")
        
        
account1 = SavingsAccount(101, 10000, "Kasangaki John", 0.2)
account2 = SavingsAccount(102, 20000, "Kasangaki Justine", 0.2)

account1.deposit(1000)
account2.deposit(5000)

account1.withdraw(50000)
account2.withdraw(4000)
 
account1.display_account_info()       
account2.display_account_info()       
            