class Product:                                  #class
    def __init__(self, name, price, quantity): #inisiliazator
        self.name = name                        #atributi
        self.price = price                       #atributi
        self.quantity = quantity                 #atributi
        
        
    def info(self):                             #metodi classa 
        return f"Tovar: {self.name}, Narx: {self.price} somoni, Dona: {self.quantity}"
    
    
    def buy(self, name, quantity):           #metodi classa
        
        if name == self.name:
            print("Chand dona mexoxed xared: ")
            if quantity <= self.quantity:
                self.quantity -= quantity
                print(f"{self.name}, {quantity}, dona xarida shud!")
                return
        return 
    
