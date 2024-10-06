class BankAccount:
    interest_rate = 0.05  # Class variable
    
    def __init__(self, account_holder, balance = 0):
        self.account_holder = account_holder
        self.balance = balance  # Instance variable
    
    #method to deposit
    def deposit(self, amount):
        self.balance += amount
    
    #method to withdraw
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds")
    
    def apply_interest(self):
        self.balance += self.balance * BankAccount.interest_rate
    
    def display_account_info(self):
        print(f"Account holder: {self.account_holder}, Balance: {self.balance}")

# Creating instances
acc1 = BankAccount("Alice")
acc2 = BankAccount("Bob")

acc1.deposit(1000)
acc1.apply_interest()
acc1.display_account_info()

acc2.deposit(2000)
acc2.withdraw(500)
acc2.apply_interest()
acc2.display_account_info()
