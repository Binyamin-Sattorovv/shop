from models.store import Store
from models.product import Product

st = Store("Магазин фруктов")       #obekt classa


st.add_tovar("Яблоко", 5, 100)

st.add_tovar("Банан", 7, 50)

print()

st.list_products()

print(st.buy("Яблоко", 10))

print()

st.search_tovar("Яблоко")

print()

st.list_products()

print(st.is_available("Банан"))

st.remove_tovar("Банан")

print()

st.list_products()