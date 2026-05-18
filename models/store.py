from models.product import Product

class Store:

    def __init__(self, name: str):

        self.name = name
        self.products = []



    def add_tovar(self, name: str, price: int, dona: int):

        # проверка существует ли товар
        for product in self.products:
            
            if product.name == name:
                
                print("Товар уже существует!")
                
                return

        tovar = Product(name, price, dona)

        self.products.append(tovar)

        print(f"{name} добавлен!")



    def remove_tovar(self, name: str):

        for product in self.products:

            if product.name == name:

                self.products.remove(product)

                print(f"{name} удалён!")

                return 
            
        return "Tovar yoft nashud!"



    def list_products(self):

        if len(self.products) == 0:
            
            print("Склад пуст!")
            
            return

        for product in self.products:
            
            print(product)



    def is_available(self, name):

        for product in self.products:

            if product.name == name:

                if product.dona > 0:
                    return "Есть в наличии"

                return "Нет в наличии"

        return "Товар не найден"
    
    
    def search_tovar(self, name: str):
        
        for product in self.products:
            
            if product.name.lower() == name.lower():
                
                return (
                    f"\nYoft shud!\n"
                    f"{product}"
                )
                
        return "Yoft nashud!"



    def buy(self, name: str, dona: int):

        for product in self.products:

            if product.name == name:

                if dona > product.dona:
                    
                    return "Недостаточно товара!"

                product.dona -= dona

                total = dona * int(product.price)

                return (
                    f"{dona} шт. куплено!\n"
                    f"Общая сумма: {total} сомони"
                )

        return "Товар не найден"