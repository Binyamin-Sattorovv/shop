class Product:               #class

    def __init__(self, name, price, dona):      #inisilizator

        self.name = name       #atribut
        
        self.__price = 0
        self.__dona = 0
        
        self.price = price
        self.dona = dona
        
        
        # Narx
    @property
    
    def price(self):
        
        return self.__price
    
    
    @price.setter
    
    def price(self, new_price):
        
        if int(new_price) < 0:
            
            print("Narx boyad az nol kalon boshad!")
            
            return
        
        self.__price = int(new_price)
        
        print("Narxi nav vorid karda shud!")
        
        
        # Dona
    @property
        
    def dona(self):
        
        return self.__dona
    
    
    @dona.setter
    
    def dona(self, new_dona):
        
        if int(new_dona) < 0:
            
            print("Dona naboyad az nol xurd boshad!")
            
            return
        
        self.__dona = int(new_dona)
        print("Dona ivaz larda shud!")
    
    
    def __str__(self):

        return (
            f"Товар: {self.name}\n"
            f"Цена: {self.price} сомони\n"
            f"Количество: {self.dona}\n"
        )

