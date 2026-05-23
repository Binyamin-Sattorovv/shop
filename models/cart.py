from dataclasses import dataclass
from models.product import Product
from models.product import LoggerMixin


@dataclass
class CartItem:
    
    product: Product
    
    dona: int
        
    
    def total_price(self):
        
        return self.product.price * self.dona
    
    
    def shipping_price(self):
        
        return self.product.shipping_price()
    
        
    def final_price(self):
        
        return (
            self.shipping_price() + self.total_price()
        )
    
    def __str__(self):
        
        return (
            f"Product: {self.product.name}\n"
            f"Quantity: {self.dona}\n"
            f"Product total: {self.total_price()}\n"
            f"Shipping: {self.shipping_price()}\n"
            f"Final: {self.final_price()}\n"
        )
        
    
class Cart(LoggerMixin):
    
    def __init__(self):
        
        self.items = []
        
    
    def add_items(self, product, dona):
        
        if product.dona < dona:
            
            return "Dona kifoya nest!"
        
        item = CartItem(product, dona)
        
        self.items.append(item)
        
        self.log(f"{product.name} aded to Korzina!")
    
    
    def show_cart(self):
        
        if len(self.items) == 0:
            
            return "Korzina xoli!"
        
        for item in self.items:
            
            print(item)
            
    
    def total_sum(self):
        
        total = 0
        
        for item in self.items:
            
            total += item.final_price()
        
        return total

    
    
    def clear_cart(self):
        
        self.items.clear()
        
        self.log("Korzina toza shud!")
    