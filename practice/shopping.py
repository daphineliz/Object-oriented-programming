class Product:
    
    def __init__(self, product_name, price, quantity_in_stock):
        self.product_name = product_name
        self.price = price
        self.quantity_in_stock = quantity_in_stock
        
    #method to display product info
    def display_product_info(self):
        print(f"Product: {self.product_name}\n, Price: {self.price}\n, Quantity: {self.quantity_in_stock}")


class ShoppingCart:
    total_carts = 0
    
    def __init__(self):
        self.items = []
        ShoppingCart.total_carts += 1
    
    def add_to_cart(self, product, quantity):
        if quantity <= self.quantity_in_stock: 
            self.items.append((product, quantity))
            self.quantity_in_stock -= quantity
            print(f"You have added {product} to your cart")
        else: 
            print(f"We dont have enough quantity in stock")
    
    
def remove_from_cart(self, product):
        for item in self.items:
            if item[0] == product:
                self.items.remove(item[0])
                self.quantity_in_stock += item[1]
                print(f"You have removed {product} from your cart")
            
        else: 
            print(f"cant find {product} in your cart")
    
def display_cart(self):
    print(f"Your shopping Cart:\n")
    for product, quantity in self.items:
        print(f"- {product} Quantity{quantity}")
    
def calculate_total(self):
    for product, quantity in self.items:
        total += product * quantity

    