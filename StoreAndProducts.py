
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
        pass

    def set_clearance(self, category, percent_discount):
        pass

class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price 
        self.category = category 
    
    def update_price(self, price): 
        self.price += price 
    
    def print_info(self):
        print("\nProduct Name: ", self.name, "\nProduct Price: $", self.price, "\nProduct Category: ", self.category)

# Store
# add product
# sell product

# Product
# update price
# print info

#creating a store
store1 = Store("Target")
# creating 4 products
product1 = Product("Toothpaste", 1.5, "bathroom")
product2 = Product("Toothbrush", 1, "bathroom")
product3 = Product("Soap", .5, "bathroom")
product4 = Product("Shampoo", 2, "bathroom")

# adding products to the store
store1.add_product(product1) 
store1.add_product(product2)
store1.add_product(product3)
store1.add_product(product4)
# printing list of products






