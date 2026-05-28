
class Store():

    def __init__(self, name):

        self.name = name
        self.products = []
        
    
    def __iter__(self):
        
        return iter(self.products)
        

                