from dataclasses import dataclass
from models.product import Product
from models.logger import logger

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
        
    
class Cart():
    
    def __init__(self):
        
        self.items = []
        
    
    def show_cart(self):
        
        if len(self.items) == 0:
            
            return "Korzina xoli!"
        
        for item in self.items:
            
            print(item)
            
    
    def clear_cart(self):
        
        self.items.clear()
        
        logger.info("Korzina xoli shud!")
        
    def __add__(self, other):
        
        new_cart = Cart()
        
        new_cart.items = (
            self.items + other.items
        )
        
        return new_cart
        
        
    def __len__(self):
        
        return len(self.items)
    