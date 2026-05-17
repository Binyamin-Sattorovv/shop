class Product:               #class

    def __init__(self, name, price, dona):      #inisilizator

        self.name = name       #atribut
        self.__price = price
        self.dona = int(dona)
        
        
    def get_price(self):
        return self.__price

    def __str__(self):

        return (
            f"Товар: {self.name}\n"
            f"Цена: {self.__price} сомони\n"
            f"Количество: {self.dona}\n"
        )

