from models.product import Product
from models.store import Store


# STORE

st = Store("Mevaho")


# ADD PRODUCTS

st.add_tovar("seb", 3, 100)
st.add_tovar("nok", 5, 200)
st.add_tovar("anor", 7, 300)

print()


# LIST

st.list_products()

print()


# BUY

print(st.buy("seb", 10))

print()


# SEARCH

print(st.search_tovar("nok"))

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