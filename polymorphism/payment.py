class Payment:
    def __init__(self, amount):
        self.amount = amount
    
    def paid(self):
        print(f"Paid: {self.amount}")
        
class Casg(Payment):
    def __init__(self, amount):
        super().__init__(amount)
        
class Momo(Payment):
    def __init__(self, amount, merchantCode):
        super().__init__(amount)
        self.merchantCode = merchantCode
        
class Visa(Payment):
    def __init__(self, amount, cvc):
        super().__init__(amount)
        self.cvc = cvc