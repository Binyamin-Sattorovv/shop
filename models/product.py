from models.error import ProductNotFoundError, OutOfStockError, ErorofPrice


class LoggerMixin:

    def log(self, message):

        print(f"[LOG]: {message}")


# PRODUCT

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
            
            raise ErorofPrice("Dona kifoya nest!")

            return

        self.__price = int(new_price)

    # DONA

    @property
    def dona(self):

        return self.__dona

    @dona.setter
    def dona(self, new_dona):

        if int(new_dona) < 0:

            raise OutOfStockError("Dona naboyad manfi boshad!")

            return

        self.__dona = int(new_dona)

    # TO DICT

    def to_dict(self):

        return {
            "type": "product",
            "name": self.name,
            "price": self.price,
            "dona": self.dona
        }

    # POLYMORPHISM

    def deliver(self):

        return "Action nest!"
    
    
    def shipping_price(self):
        
        return 0

    def __str__(self):

        return (
            f"PRODUCT\n"
            f"\n"
            f"Name: {self.name}\n"
            f"Narx: {self.price} somoni\n"
            f"Dona: {self.dona}\n"
        )


# DIGITAL PRODUCT

class DigitalProduct(Product):

    def __init__(
        self,
        name,
        price,
        dona,
        file_size
    ):

        super().__init__(name, price, dona)

        self.file_size = file_size

    # OVERRIDE

    def deliver(self):

        return "delivered"

    # TO DICT

    def to_dict(self):

        return {
            "type": "digital",
            "name": self.name,
            "price": self.price,
            "dona": self.dona,
            "file_size": self.file_size
        }
        
    
    def shipping_price(self):
        
        return 0

    def __str__(self):

        return (
            f"DIGITAL PRODUCT\n"
            f"\n"
            f"Name: {self.name}\n"
            f"Price: {self.price}\n"
            f"Dona: {self.dona}\n"
            f"File Size: {self.file_size} MB\n"
        )


# PHYSICAL PRODUCT

class PhysicalProduct(Product):

    def __init__(
        self,
        name,
        price,
        dona,
        weight
    ):

        super().__init__(name, price, dona)

        self.weight = weight

    # OVERRIDE

    def deliver(self):

        return "delivered"
        
        
    # TO DICT

    def to_dict(self):

        return {
            "type": "physical",
            "name": self.name,
            "price": self.price,
            "dona": self.dona,
            "weight": self.weight
        }
        
    def shipping_price(self):
        
        return self.weight * 10
    
    
    def __str__(self):

        return (
            f"PHYSICAL PRODUCT\n"
            f"\n"
            f"Name: {self.name}\n"
            f"Price: {self.price}\n"
            f"Dona: {self.dona}\n"
            f"Weight: {self.weight} KG\n"
        )
