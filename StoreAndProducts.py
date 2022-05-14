
from math import prod
from unicodedata import name


class Store:
    def __init__(self, name):
        self.name = name 
        self.listOfProducts = []

    def add_product(self, new_product):
        self.listOfProducts.append(new_product) 

    def sell_product(self, id):
        self.listOfProducts.pop(id) 

    def inflation(self, percent_increase):
        for product in self.listOfProducts:
            product.price = product.price + (product.price * percent_increase) 

    def set_clearance(self, category, percent_discount):
        for product in self.listOfProducts:
            if(category == product.category):
                product.price = product.price - (product.price * percent_discount) 
            else: 
                pass 
    
    def print_all_items(self):
        for product in self.listOfProducts:
            print("\nProduct Name: ", product.name, "\nProduct Price: $", product.price, "\nProduct Category: ", product.category)

class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price 
        self.category = category 
    
    def update_price(self, price): 
        self.price += price 
    
    def print_info(self):
        print("\nProduct Name: ", self.name, "\nProduct Price: $", self.price, "\nProduct Category: ", self.category)

    def getName(self):
        return self.name

    def getPrice(self): 
        return self.price 

    def getCategory(self):
        return self.category 


#creating a store
store1 = Store("Target")

# creating products
product1 = Product("Toothpaste", 2, "bathroom")
product2 = Product("Toothbrush", 1, "bathroom")

# adding products to the store
store1.add_product(product1) 
store1.add_product(product2)

# inflation increase
store1.inflation(.5) 

# setting clearance
store1.set_clearance("bathroom", .5) 

# printing list of products
store1.print_all_items()






