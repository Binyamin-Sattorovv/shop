class Product:
    
    def __init__(self, name, price, dona):
        
        self.name = name
        self.price = price
        self.dona = dona
        
        self.tovarho = []
    
    
    def info(self):
        
        return (
            f"Товар: {self.name}\n"
            f"Цена: {self.price} сомони\n"
            f"Количество: {self.dona}"
        )
    
     
    def add_tovar(self, name: str, dona: int):
       
       tovar = list(zip(name, dona))
       
       self.tovarho.append(tovar)
       print("Tovarho vorid karda shud!")
       
    
    def remove_dona(self, dona: int):
        
        if dona > self.dona:
            return "In qadar mahsulot nest!"
        
        self.dona -= dona
        return f"{dona} dona udalit karda shud!"
    
    
    def is_available(self):
        
        return f"{self.dona}, dona hast" if self.dona > 0 else "Nest"
    
    
    def buy(self, name: str, dona: int):
        
        if name != self.name:
            return "Nodurust!"
        
        if dona > self.dona:
            return "Kolichestvo nest!"
        
        self.dona -= dona
        
        total = dona * self.price
        
        return (
            f"{dona} dona xarid shud!\n"
            f"Jam: {total} somoni"
        )



pr = Product("seb", 5, 55)

print(pr.info())
print()

name = input("nom: ")
dona = input("dona: ")
print(pr.add_tovar(name, dona))
print()

print(pr.remove_dona(4))
print()

print(pr.is_available())
print()

print(pr.buy("seb", 12))

