from models.order import OrderStatus
from models.logger import logger
from models.error import OutOfStockError

class OrderService:
    
    @staticmethod
    def total_sum(order):
        
        total = 0
        
        for item in order.items:
            
            total += item.total_price()
            total += item.shipping_price()
            
        return total
    
    
    @staticmethod
    def pay_order(order):

        for item in order.items:

            if item.product.dona < item.dona:

                raise OutOfStockError(
                    f"{item.product.name} kifoya nest!"
                )

        for item in order.items:

            item.product.dona -= item.dona

        amount = OrderService.total_sum(order)

        result = order.payment.pay(amount)

        order.status = OrderStatus.PAID

        return result
    
    @staticmethod
    def delivery_order(order):
        
        order.status = OrderStatus.DELIVERED
        
        logger.info("Delivered")
        
        