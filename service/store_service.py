import json

from models.logger import logger
from models.product import Product, PhysicalProduct, DigitalProduct

from models.error import ProductNotFoundError, OutOfStockError, ErorofPrice


class StoreService:
    
    @staticmethod
    def add_tovar(store, product):
        
        for item in store.products:
            
            if item.name.lower() == product.name.lower():
                
                return "Tovar Hast!"
            
        store.products.append(product)
        
        logger.info(f"{product.name}, aded")
    
    
    @staticmethod
    def remove_tovar(store, name):
        
        for product in store.products:
            
            if product.name.lower() == name.lower():
                
                store.products.remove(product)
                
                logger.info(f"{product.name}, removed!")
                
                return
        raise ProductNotFoundError("Product yoft nashud!")
    
    @staticmethod
    def list_products(store):
        
        if len(store.products) == 0:
            
            return "Sklad xoli!"
        
        for product in store.products:
            
            print(product)
            
    
    @staticmethod
    def search_tovar(store, name):
        
        for product in store.products:
            
            if product.name.lower() == name.lower():
                
                print(f"Yoft shud: {product}")
                return
                
        raise ProductNotFoundError("Yoft nashud!")
    
    @staticmethod
    def buy (store, name, dona, payment_method):
        
        for product in store.products:
            
            if product.name.lower() == name.lower():
                
                if product.dona < dona:
                    
                    return "Dona kifoya nest!"
                
                product.dona -= dona
                    
                total = dona * product.price
                
                payment_result = payment_method.pay(total)
                
                shipping_result = product.shipping_price()
                
                logger.info(f"{product.name}, sold!")
                
                return (
                    f"{product.name}, {dona}, dona xarid shud!\n"
                    f"{payment_result}\n"
                    f"Shipping: {shipping_result}\n"
                )
        
        raise ProductNotFoundError("Yoft nashud!")
    
    
    @staticmethod
    def save_json(store):
        
        data = []
        
        for product in store.products:
            
            data.append(product.to_dict())
            
        
        with open("shop/data/products.json", "w", encoding="utf-8") as file:
            
            json.dump(data, file, indent=4, ensure_ascii=False)
            
        logger.info("Product saved!")
        
        
    @staticmethod
    def load_json(store):
        
        store.products.clear()
        
        with open("shop/data/products.json", "r", encoding="utf-8") as file:
            
            data = json.load(file)
            
        for product_data in data:
            
            if product_data["type"] == "product":
                
                product = Product.from_dict(product_data)
                
            elif product_data["type"] == "digital":
                
                product = DigitalProduct(
                    product_data["name"],
                    product_data["price"],
                    product_data["dona"],
                    product_data["file_size"],
                )
                
            elif product_data["type"] == "physical":
                
                product = PhysicalProduct(
                    product_data["name"],
                    product_data["price"],
                    product_data["dona"],
                    product_data["weight"],
                )
        store.products.append(product)
        
        logger.info("Product loaded!")

                
                
            
            
        
                
                
    
            
                
    