import json

from models.product import LoggerMixin

from models.product import Product, PhysicalProduct, DigitalProduct

from models.error import ProductNotFoundError, OutOfStockError, ErorofPrice



class Store(LoggerMixin):

    def __init__(self, name):

        self.name = name
        self.products = []

    def add_tovar(self, product):

        for item in self.products:

            if item.name.lower() == product.name.lower():
                
                return "Tovar alakay hast!"

        self.products.append(product)

        self.log(f"{product.name} added!")

    def remove_tovar(self, name):

        for product in self.products:

            if product.name.lower() == name.lower():

                self.products.remove(product)

                self.log(f"{name} removed!")

                return

        raise ProductNotFoundError("Product nest!")
    

    def list_products(self):

        if len(self.products) == 0:
            return "Sklad xoli!"

        for product in self.products:
            print(product)

    def search_tovar(self, name):

        for product in self.products:

            if product.name.lower() == name.lower():

                return (
                    f"Yoft shud!\n"
                    f"{product}"
                )

        raise ProductNotFoundError("Product nest!")

    def buy(self, name, dona, payment_method):

        for product in self.products:

            if product.name.lower() == name.lower():

                if product.dona < dona:
                    return "Dona kifoya nest!"

                product.dona -= dona

                total = dona * product.price

                payment_result = payment_method.pay(total)

                shiping_price = product.shipping_price()

                self.log(f"{product.name} sold!")

                return (
                    f"{dona} dona {product.name} xarid shud!\n"
                    f"\n"
                    f"{payment_result}\n"
                    f"{shiping_price}\n"
                )

        raise ProductNotFoundError("Product nest!")

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

        self.log("Products saved!")

    def load_products(self):

        self.products.clear()

        with open("products.json", "r") as file:

            data = json.load(file)

        for product_data in data:

            if product_data["type"] == "product":

                product = Product.from_dict(product_data)

            elif product_data["type"] == "digital":

                product = DigitalProduct(
                    product_data["name"],
                    product_data["price"],
                    product_data["dona"],
                    product_data["file_size"]
                )

            elif product_data["type"] == "physical":

                product = PhysicalProduct(
                    product_data["name"],
                    product_data["price"],
                    product_data["dona"],
                    product_data["weight"]
                )

            self.products.append(product)

        self.log("Products loaded!")
        

                