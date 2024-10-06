#class product
class Product:
    def __init__(self, product_name, price, quantity_in_stock):
        self.product_name = product_name
        self.price = price
        self.quantity_in_stock = quantity_in_stock
    
    def display_product_info(self):
        print(f"Product: {self.product_name}, Price: {self.price}, Quantity: {self.quantity_in_stock}")

#class shopping cart
class ShoppingCart:
    total_carts = 0  # Class variable
    
    def __init__(self):
        self.items = []
        ShoppingCart.total_carts += 1
    
    #method to add products to cart
    def add_to_cart(self, product, quantity):
        if product.quantity_in_stock >= quantity:
            self.items.append((product, quantity))
            product.quantity_in_stock -= quantity
            print(f"\n You have added {product.product_name} to your cart")
        else:
            print(f"Not enough stock for {product.product_name}")

    
    #method to remove products from cart
    def remove_from_cart(self, product):
        for item in self.items:
            if item[0] == product:
                self.items.remove(item)
                product.quantity_in_stock += item[1]
        
        print(f"\nYou have removed {product.product_name} from your cart")
    
    #method to display priducts in cart
    def display_cart(self):
        for product, quantity in self.items:
            print(f"\nCart:")
            print(f"{product.product_name} - {quantity}")
    
    #method to calculate total
    def calculate_total(self):
        total = 0
        for product, quantity in self.items:
            total += product.price * quantity
        return total

# Create products
prod1 = Product("Laptop", 1000, 5)
prod2 = Product("Phone", 500, 10)
prod3 = Product("Headphones", 100, 20)

# Create shopping carts
cart1 = ShoppingCart()
cart2 = ShoppingCart()

cart1.add_to_cart(prod1, 1)
cart1.add_to_cart(prod2, 2)
cart1.remove_from_cart(prod1)
cart1.display_cart()
print("Total:", cart1.calculate_total())

cart2.add_to_cart(prod3, 3)
cart2.display_cart()
print("Total:", cart2.calculate_total())
