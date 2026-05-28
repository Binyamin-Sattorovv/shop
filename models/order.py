from enum import Enum

class OrderStatus(Enum):
    
    PENDING = "Pending"
    PAID = "Peid"
    DELIVERED = "Delivered"
    
    
    
class Order():
    
    order_id = 1
    
    def __init__(self, user, cart, payment):
        
        self.id = Order.order_id
        
        Order.order_id += 1
        
        self.user = user
        self.items = cart.items.copy()
        self.payment = payment
        
        self.status = OrderStatus.PENDING
        
        user.orders.append(self)
        
    
    
    def show_order(self):
        
        print(f"Order id: {self.id}")
        print(f"User: {self.user.username}")
        print(f"Status: {self.status.value}")
        
        for item in self.items:
            
            print(item)
        
        
    
    def __str__(self):
        
        return (
            f"Order: {self.id}\n"
            f"User: {self.user.username}\n"
            f"Status: {self.status.value}\n"
            f"Items: {len(self.items)}\n"
            f"Total: {self.total_sum()}, somoni\n"
        )
        
        