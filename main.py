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

cart.add_product(p1, 3)
cart.add_product(p2, 2)
print()

cart.show_cart()
print()

print(cart.total_sum())
print()

cart.clear_cart()
