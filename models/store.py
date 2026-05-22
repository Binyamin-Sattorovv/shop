import json

from models.product import (
    Product,
    DigitalProduct,
    PhysicalProduct,
    LoggerMixin,
)

from enum import Enum


class Store(LoggerMixin):

    def __init__(self, name):

        self.name = name
        self.products = []

    def add_tovar(self, product):

        for item in self.products:

            if item.name.lower() == product.name.lower():
                return "Tovar alakay hast!"

        self.products.append(product)

        self.log(f"{product.name} added!")

    def remove_tovar(self, name):

        for product in self.products:

            if product.name.lower() == name.lower():

                self.products.remove(product)

                self.log(f"{name} removed!")

                return

        return "Tovar yoft nashud!"
    

    def list_products(self):

        if len(self.products) == 0:
            return "Sklad xoli!"

        for product in self.products:
            print(product)

    def search_tovar(self, name):

        for product in self.products:

            if product.name.lower() == name.lower():

                return (
                    f"Yoft shud!\n"
                    f"{product}"
                )

        return "Tovar yoft nashud!"

    def buy(self, name, dona, payment_method):

        for product in self.products:

            if product.name.lower() == name.lower():

                if product.dona < dona:
                    return "Dona kifoya nest!"

                product.dona -= dona

                total = dona * product.price

                payment_result = payment_method.pay(total)

                shiping_price = product.shipping_price()

                self.log(f"{product.name} sold!")

                return (
                    f"{dona} dona {product.name} xarid shud!\n"
                    f"\n"
                    f"{payment_result}\n"
                    f"{shiping_price}\n"
                )

        return "Tovar yoft nashud!"

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

        self.log("Products saved!")

    def load_products(self):

        self.products.clear()

        with open("products.json", "r") as file:

            data = json.load(file)

        for product_data in data:

            if product_data["type"] == "product":

                product = Product.from_dict(product_data)

            elif product_data["type"] == "digital":

                product = DigitalProduct(
                    product_data["name"],
                    product_data["price"],
                    product_data["dona"],
                    product_data["file_size"]
                )

            elif product_data["type"] == "physical":

                product = PhysicalProduct(
                    product_data["name"],
                    product_data["price"],
                    product_data["dona"],
                    product_data["weight"]
                )

            self.products.append(product)

        self.log("Products loaded!")
        
    

class CartItem:
    
    def __init__(self, product, dona):
        
        self.product = product
        self.dona = dona
        
        
    def delivery(self):
        
        return self.product.deliver()
    
    
    def total_price(self):
        
        product_total = self.dona * self.product.price
        
        shiping = self.product.shipping_price()
        
        return product_total + shiping
    
    
    def shipping_price(self):
        
        if isinstance(self.product, PhysicalProduct):
            
            return self.shipping_price()
        
        return 0
    
    
    def __str__(self):
        
        return (
            f"Product: {self.product}\n"
            f"Dona: {self.dona}\n"
            f"Total: {self.total_price()}\n"
            f"Status: {self.delivery()}"
        )
        

class Cart(LoggerMixin):
    
    def __init__(self):
        
        self.items = []
        
        
    def add_items(self, product, dona):
        
        if product.dona < dona:
            
            return "Dona kifoya nest!"
        
        item = CartItem(product, dona)
        
        self.items.append(item)
    
        
        self.log(f"{product.name}, ba Korzina vorid shud!")
        
    
    def show_cart(self):
        
        if len(self.items) == 0:
            
            return "Korzina Xoli!"
        
        for item in self.items:
            
            print(item)
            
            
    def total_sum(self):
        
        total = 0 
        
        for item in self.items:
            
            total += item.total_price()
        return total 
        
        
        
    def clear_cart(self):
        
        self.items.clear()
        
        self.log("Korzina Xoli shud!")
        


class OrderStatus(Enum):
    
    PENDING = "pending"
    DELIVERED = "delivered"
    SHIPPING = "shiping"
    

class User:
    
    def __init__(self, username):
        
        self.username = username
        
        self.cart = Cart()
        
        self.order = []
        
    
    def __str__(self):
        
        return (
            f"Username: {self.username}"
            f"Order: {self.order}"
        )
        

class Order(LoggerMixin):
    
    user_id = 1
    
    def __init__(self, user, cart, payment):
        
        self.id= Order.user_id
        
        Order.user_id += 1
        
        self.user = user
        
        self.items = cart.items.copy()
        
        self.payment = payment
        
        self.status = OrderStatus.PENDING
        
        
    def total_sum(self):

        total = 0

        for item in self.items:

            total += item.total_price()

            if isinstance(item.product, PhysicalProduct):

                total += item.product.shipping_price()

        return total
    
    def pay_order(self):
        
        amount = self.total_sum()
        
        payment_result = self.payment.pay(amount)
        
        self.status = OrderStatus.PENDING
        
        self.log(f"Order #{self.id}, pardoxt shud!")
        
        return payment_result
    
    
    def show_order(self):
        
        print(f"Order Id: {self.id}")
        print(f"User: {self.user}")
        print(f"Status: {self.status}")
        
        for item in self.items:
            
            print(item)
            
        print(f"TOTAL: {self.total_sum()}")
        
        
    def delivery_order(self):
        
        self.status = OrderStatus.DELIVERED
        
        self.log(f"Order #{self.id}, delivered")
        
        return "Zakaz dostavka shud!"
    
    
    def __str__(self):
            
        return (
                f"Order: {self.id}\n"
                f"User: {self.user.username}\n"
                f"Status: {self.status.value}\n"
                f"Items: {len(self.items)}\n"
        )




        
        
        