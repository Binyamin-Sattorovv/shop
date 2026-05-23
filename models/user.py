from models.cart import Cart

class User:
    
    def __init__(self, username):
        
        self.username = username
        
        self.cart = Cart()
        
        self.orders = []
        
    
    def __str__(self):
        
        return (
            f"User: {self.username}\n"
            f"Orders: {self.orders}\n"
        ) 
        
        
