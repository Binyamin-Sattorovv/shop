import json
from models.product import Product
from abc import ABC, abstractmethod


class DigitalProduct(Product):
    
    def __init__(self, name, price, dona, file_size):
        
        super().__init__(name, price, dona)
        
        self.file_size = file_size
        
    
    def action(self):
        
        return (
            f"{self.name}: download shud!\n"
            f"File size: {self.file_size}, mb\n"
        )
        
        
    def __str__(self):
            
        return (
            
            f"DIIGTAL PRODUCT\n"
            f"\n"
            f"Name: {self.name}\n"
            f"Price: {self.price}\n"
            f"Dona: {self.dona}\n"
            f"File size: {self.file_size}\n"
        )
        
        
    
class PyshicalProduct(Product):
    
    def __init__(self, name, price, dona, weight):
        
        super().__init__(name, price, dona)
        
        self.weight = weight
        
        
    def action(self):
        
        shipping =  self.weight * 10

        
        return (
            f"{self.name}, dostavka shuda istodaast!\n"
            f"Narxi dostavka: {shipping}, somoni\n"
        )
        
        
    def __str__(self):
        
        return (
            
            f"PYSHICALPRODUCT\n"
            f"\n"
            f"Name: {self.name}\n"
            f"Price: {self.price}\n"
            f"Dona: {self.dona}\n"
            f"Vazn: {self.weight}, kg\n"
        )
        
           
class Payment(ABC):
    
    @abstractmethod
    def pay(self, amount):
        pass 
    
    

class ClickPayment(Payment):
    
    def pay(self, amount):
        return (
            f"CashPayment kabul shud!\n"
            f"Summa: {amount}, somoni!\n"
        )
        

class CardPayment(Payment):
    
    def pay(self, amount):
        return (
            f"CardPayment kabul shud!\n"
            f"Summa: {amount}, somoni!\n"
        )
    

class CashPayment(Payment):
    
    def pay(self, amount):
        return (
            f"CashPayment kabul shud!\n"
            f"Summa: {amount}, somoni!\n"
        )
        
        
        
class Store:

    def __init__(self, name):

        self.name = name
        self.products = []

    # ADD

    def add_tovar(self, product):

        for item in self.products:

            if item.name.lower() == product.name.lower():
                return "Tovar alakay hast!"

        self.products.append(product)

        print(f"{product.name} vorid karda shud!")

    # REMOVE

    def remove_tovar(self, name):

        for product in self.products:

            if product.name.lower() == name.lower():

                self.products.remove(product)

                print(f"{name} udalil shud!")

                return

        return "Tovar yoft nashud!"

    # LIST

    def list_products(self):

        if len(self.products) == 0:
            return "Sklad xoli!"

        for product in self.products:
            print(product)

    # SEARCH

    def search_tovar(self, name):

        for product in self.products:

            if product.name.lower() == name.lower():

                return (
                    f"Yoft shud!\n"
                    f"{product}"
                )

        return "Tovar yoft nashud!"

    # AVAILABLE

    def is_available(self, name):

        for product in self.products:

            if product.name.lower() == name.lower():

                if product.dona > 0:
                    return "Dar anbor hast!"

                return "Tamom shud!"

        return "Tovar yoft nashud!"

    # BUY

    def buy(self, name, dona, method_payment):

        for product in self.products:

            if product.name.lower() == name.lower():

                if product.dona < dona:
                    return "Dona kifoya nest!"

                product.dona -= dona

                total = dona * product.price
                result_method = method_payment.pay(total)
                delivery = product.action()
                

                return (
                    f"{dona} dona {product.name}, xarid shud!\n"
                    f"Summa: {total} somoni"
                    f"Result: {result_method}\n"
                    f"Delivery: {delivery}\n"
                )

        return "Tovar yoft nashud!"

    # SAVE JSON

    def save_products(self):

        data = []

        for product in self.products:

            data.append(product.to_dict())

        with open("products.json", "w") as file:

            json.dump(
                data,
                file,
                indent=4,
                ensure_ascii=False
            )

        print("Products saved!")

    # LOAD JSON

    def load_products(self):

        self.products.clear()

        with open("products.json", "r") as file:

            data = json.load(file)

        for product_data in data:

            product = Product.from_dict(product_data)

            self.products.append(product)

        print("Products loaded!")

