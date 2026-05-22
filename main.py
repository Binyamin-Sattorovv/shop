from models.product import *
from models.payment import *
from models.store import*


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
    5,
    3
)

p3 = PhysicalProduct(
    "Seb",
    23,
    3,
    100
)

p4 = Product(
    "Video",
    14,
    600,
)


# ADD

st.add_tovar(p1)
st.add_tovar(p2)
st.add_tovar(p3)


print()


# LIST

st.list_products()

print()


# PAYMENTS

click = ClickPayment()

card = CardPayment()

cash = CashPayment()


# BUY

print(st.buy("Laptop", 1, card))

print()

print(st.buy("Python Course", 1, click))

print()


# SEARCH

print(st.search_tovar("Seb"))

print()

# USER

user1 = User("Said")


# ADD TO CART

user1.cart.add_items(p1, 2)
user1.cart.add_items(p2, 1)
user1.cart.add_items(p3, 5)

print()


# SHOW CART

user1.cart.show_cart()

print(user1.cart.total_sum())

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

print(order1.pay_order())

print()


# DELIVER ORDER

print(order1.delivery_order())

print()


# FINAL STATUS

print(order1)


# SAVE

st.save_products()

print()


# LOAD

st.load_products()

print()


# LIST AGAIN

st.list_products()

print()


# TOTAL PRODUCTS

print(Product.total_products)

print()


# STATICMETHOD

print(Product.validate_discount(20))
print(Product.validate_discount(120))
print()


cart = Cart()

cart.add_items(p1, 3)
cart.add_items(p2, 2)
print()

cart.show_cart()
print()

print(cart.total_sum())
print()

cart.clear_cart()
