class Product:

    total_products = 0

    def __init__(self, name: str, price: int, dona: int):

        self.name = name

        self.__price = 0
        self.__dona = 0

        self.price = price
        self.dona = dona

        Product.total_products += 1

    # CLASSMETHOD

    @classmethod
    def from_dict(cls, data):

        return cls(
            data["name"],
            data["price"],
            data["dona"]
        )

    # STATICMETHOD

    @staticmethod
    def validate_discount(discount):

        if discount < 0 or discount > 100:
            return "Discount xato!"

        return "Discount durust!"

    # PRICE

    @property
    def price(self):

        return self.__price

    @price.setter
    def price(self, new_price):

        if int(new_price) < 0:
            print("Narx naboyad manfi boshad!")
            return

        self.__price = int(new_price)

    # DONA

    @property
    def dona(self):

        return self.__dona

    @dona.setter
    def dona(self, new_dona):

        if int(new_dona) < 0:
            print("Dona naboyad manfi boshad!")
            return

        self.__dona = int(new_dona)

    # TO DICT

    def to_dict(self):

        return {
            "name": self.name,
            "price": self.price,
            "dona": self.dona
        }
        
        
    def action(self):
        
        return "Action xoli!"
        

    def __str__(self):

        return (
            f"Name: {self.name}\n"
            f"Narx: {self.price} somoni\n"
            f"Dona: {self.dona}\n"
        )


