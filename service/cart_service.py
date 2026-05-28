from models.cart import CartItem

from models.logger import logger

class CartService:
    
    @staticmethod
    def add_items(cart, product, dona):
        
        if dona < 0:
            
            return "Dona kifoya nest!"
        
        item = CartItem(product, dona)
        
        cart.items.append(item)
        
        logger.info(f"{product.name}, ba korzina vorid shud!")
        
    
    @staticmethod
    def total_sum(cart):
        
        total = 0
        
        for item in cart.items:
            
            total += item.final_price()
            
        return total
    
    @staticmethod
    def show_cart(cart):
        
        if len(cart.items) == 0:
            
            return "Sklad Xoli!"
        
        for item in cart.items:
            
            print(item)
    

    
    
        
        