class Product:               #class

    def __init__(self, name, price, dona):      #inisilizator

        self.name = name       #atribut
        self.price = int(price)
        self.dona = int(dona)

    def __str__(self):

        return (
            f"Товар: {self.name}\n"
            f"Цена: {self.price} сомони\n"
            f"Количество: {self.dona}\n"
        )

