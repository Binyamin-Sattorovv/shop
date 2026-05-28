from models.store import Store
from models.product import DigitalProduct, PhysicalProduct, Product
from models.payment import ClickPayment, CashPayment, CardPayment
from models.user import User
from models.order import Order
from models.cart import Cart
from service.store_service import StoreService
from service.order_service import OrderService
from service.cart_service import CartService


# STORE
st = Store("Mevaho")


# PRODUCTS

p1 = DigitalProduct(
    "Python Course",
    1200,
    50,
    1500
)

p2 = PhysicalProduct(
    "Laptop",
    12000,
    567,
    35
)

p3 = PhysicalProduct(
    "Seb",
    23,
    456,
    100
)

p4 = Product(
    "Video",
    14,
    600,
)

p5 = Product(
    "Bozi",
    12,
    456,
)


# ADD

StoreService.add_tovar(st, p1)
StoreService.add_tovar(st, p2)
StoreService.add_tovar(st, p3)
StoreService.add_tovar(st, p3)
StoreService.add_tovar(st, p5)



print()


# LIST

StoreService.list_products(st)

print()


# PAYMENTS

click = ClickPayment()

card = CardPayment()

cash = CashPayment()


# BUY

print(StoreService.buy(st, "Laptop", 1, card))

print()

print(StoreService.buy(st, "Python Course", 1, click))

print()


# SEARCH

print(StoreService.search_tovar(st, "Seb"))

print()

# USER

user1 = User("Said")


# ADD TO CART
CartService.add_items(user1.cart, p1, 2)
CartService.add_items(user1.cart, p2, 3)
CartService.add_items(user1.cart, p3, 4)

print()


# SHOW CART


CartService.show_cart(user1.cart)
print()

print(CartService.total_sum(user1.cart))

print()


# CREATE ORDER

order1 = Order(
    user1,
    user1.cart,
    card
)


# SHOW ORDER

order1.show_order()

print()


# PAY ORDER

print(OrderService.pay_order(order1))

print()


# DELIVER ORDER

print(OrderService.delivery_order(order1 ))

print()


# FINAL STATUS

print(OrderService.total_sum(order1))


# SAVE

StoreService.save_json(st)

print()


# LOAD

StoreService.load_json(st)

print()


# LIST AGAIN

StoreService.list_products(st)

print()


# TOTAL PRODUCTS

print(Product.total_products)

print()


# STATICMETHOD

print(Product.validate_discount(20))
print(Product.validate_discount(120))
print()


cart = Cart()
cart2 = Cart()

CartService.add_items(user1.cart, p3, 1)
CartService.add_items(user1.cart, p1, 3)
CartService.add_items(user1.cart, p2, 2)
print()

cart.show_cart()
print()

print(CartService.total_sum(user1.cart))
print()

print(len(cart))
print()

cart3 = cart + cart2

cart3.show_cart()

for product in st:
    
    print(product)
    

print(p4 == p5)
print()



cart.clear_cart()