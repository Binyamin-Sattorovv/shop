from enum import Enum
from models.product import LoggerMixin



class OrderStatus(Enum):
    
    PENDING = "Pending"
    PAID = "Peid"
    DELIVERED = "Delivered"
    
    
    
class Order(LoggerMixin):
    
    order_id = 1
    
    def __init__(self, user, cart, payment):
        
        self.id = Order.order_id
        
        Order.order_id += 1
        
        self.user = user
        self.items = cart.items.copy()
        self.payment = payment
        
        self.status = OrderStatus.PENDING
        
        user.orders.append(self)
        
    
    def total_sum(self):
        
        total = 0
        
        for item in self.items:
            
            total += item.total_price()
            total += item.shipping_price()
            
        return total
    
    
    def pay_order(self):
        
        for item in self.items:

            item.product.dona -= item.dona
    
        amount = self.total_sum()
        
        payment_result = self.payment.pay(amount)
        self.status = OrderStatus.PAID
        
        self.log(f"Order #{self.id} paid!")
        
        return payment_result      
        
        
    def delivery_order(self):
        
        self.status = OrderStatus.DELIVERED
        
        self.log(f"Order #{self.id}, delivered!")
        
        return "Zakaz dostavka shud!"
    
    
    def show_order(self):
        
        print(f"Order id: {self.id}")
        print(f"User: {self.user.username}")
        print(f"Status: {self.status.value}")
        
        for item in self.items:
            
            print(item)
            
        print(f"TOTAL: {self.total_sum()}, somoni")
        
    
    def __str__(self):
        
        return (
            f"Order: {self.id}\n"
            f"User: {self.user.username}\n"
            f"Status: {self.status.value}\n"
            f"Items: {len(self.items)}\n"
            f"Total: {self.total_sum()}, somoni\n"
        )