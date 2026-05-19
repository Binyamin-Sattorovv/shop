import json
from models.product import Product


class Store:

    def __init__(self, name):

        self.name = name
        self.products = []

    # ADD
    

    def add_tovar(self, name: str, price: int, dona: int):

        for product in self.products:

            if product.name.lower() == name.lower():
                return "Tovar alakay hast!"

        self.products.append(Product(name, price, dona))

        print(f"{name} vorid karda shud!")

    # REMOVE

    def remove_tovar(self, name):

        for product in self.products:

            if product.name.lower() == name.lower():

                self.products.remove(product)

                print(f"{name} udalil shud!")

                return

        return "Tovar yoft nashud!"

    # LIST

    def list_products(self):

        if len(self.products) == 0:
            return "Sklad xoli!"

        for product in self.products:
            print(product)

    # SEARCH

    def search_tovar(self, name):

        for product in self.products:

            if product.name.lower() == name.lower():

                return (
                    f"Yoft shud!\n"
                    f"{product}"
                )

        return "Tovar yoft nashud!"

    # AVAILABLE

    def is_available(self, name):

        for product in self.products:

            if product.name.lower() == name.lower():

                if product.dona > 0:
                    return "Dar anbor hast!"

                return "Tamom shud!"

        return "Tovar yoft nashud!"

    # BUY

    def buy(self, name, dona):

        for product in self.products:

            if product.name.lower() == name.lower():

                if product.dona < dona:
                    return "Dona kifoya nest!"

                product.dona -= dona

                total = dona * product.price

                return (
                    f"{dona} dona {product.name}, xarid shud!\n"
                    f"Summa: {total} somoni"
                )

        return "Tovar yoft nashud!"

    # SAVE JSON

    def save_products(self):

        data = []

        for product in self.products:

            data.append(product.to_dict())

        with open("products.json", "w") as file:

            json.dump(
                data,
                file,
                indent=4,
                ensure_ascii=False
            )

        print("Products saved!")

    # LOAD JSON

    def load_products(self):

        self.products.clear()

        with open("products.json", "r") as file:

            data = json.load(file)

        for product_data in data:

            product = Product.from_dict(product_data)

            self.products.append(product)

        print("Products loaded!")
