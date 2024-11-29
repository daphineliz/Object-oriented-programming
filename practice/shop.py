class ShopItem:
    def __init__(self, name, price, stock_quantity):
        if stock_quantity < 0:
             raise ValueError("Stock quantity cannot be negative.")

        assert stock_quantity >=0, f"We are out of stock!!!!!!"
    
        self.name = name
        self.price = price
        self.stock_quantity = stock_quantity
        
class Electronics(ShopItem):
    def __init__(self, name, price, stock_quantity, warrantyPeriod):
        super().__init__(name, price, stock_quantity)
        self.warrantyPeriod = warrantyPeriod
        
    #method that reduces stock
    def sell_item(self, quantity):
        if quantity <= self.stock_quantity:
            self.stock_quantity -= quantity
            print(f"{quantity} {self.name} has been sold")
            
        else:
            print(f"Not enough stock. Only {self.stock_quantity} items are available")
            
   #method to display item info and current stock
    def display_item_info(self):
        print(f"Name: {self.name}")
        print(f"Price: {self.price}")
        print(f"Stock Quantity: {self.stock_quantity}")
        print(f"Warranty Period: {self.warrantyPeriod}")
        
            
radio = Electronics("Radio", 2000, 0, "2 years")
earphones = Electronics("Earphones", 1000, -15, "1 year")

radio.sell_item(5)
earphones.sell_item(20)

radio.display_item_info()

 