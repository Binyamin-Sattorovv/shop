from models.product import Product 
from models.store import Store, DigitalProduct, PyshicalProduct, CashPayment, CardPayment, ClickPayment


# STORE

st = Store("Mevaho")


# ADD PRODUCTS


print()

p1 = DigitalProduct(
    "Python cources",
    1234,
    45,
    24
)

print()

p2 = PyshicalProduct(
    "Laptop",
    1234,
    100,
    5
)

p3 = Product("seb", 3, 100)
p4 = Product("nok", 5, 200)
p5 = Product("anor", 7, 300)


st.add_tovar(p1)
st.add_tovar(p2)
st.add_tovar(p3)
st.add_tovar(p4)
st.add_tovar(p5)

print()


# LIST

st.list_products()

print()

print(p1.action())
print(p2.action())
print()

# BUY
click = ClickPayment()
cash = CashPayment()
card = CardPayment()




print(st.buy("seb", 10, cash))
print(st.buy("Laptop", 1, card))

print()


# SEARCH

print(st.search_tovar("nok"))
print(st.search_tovar("Laptop"))

print()


# AVAILABLE

print(st.is_available("anor"))

print()


# REMOVE

st.remove_tovar("nok")

print()


# LIST AGAIN

st.list_products()

print()


# CLASS ATTRIBUTE

print(Product.total_products)

print()


# CLASSMETHOD

data = {
    "name": "banana",
    "price": 9,
    "dona": 500
}

new_product = Product.from_dict(data)

print(new_product)

print()


# STATICMETHOD

print(Product.validate_discount(20))
print(Product.validate_discount(120))

print()


# SAVE

st.save_products()

print()


# LOAD

st.load_products()

print()


# LIST AFTER LOAD

st.list_products()