from database.db import cursor, connection

class ProductRepository:
    
    @staticmethod
    def save(product):
        
        cursor.execute(
        """
        INSERT INTO products(
            name,
            price,
            dona,
            product_type
        )
        VALUES (?, ?, ?, ?)
        """, (
            product.name,
            product.price,
            product.dona,
            product.__class__.__name__
            
        ))
        
        connection.commit()
        
        
    @staticmethod
    def get_all():
        
        cursor.execute(
        """
        SELECT * FROM products
        """
        )
        
        return cursor.fetchall()
    
    
    @staticmethod
    def get_by_name(name):
        
        cursor.execute(
        """
        SELECT * FROM products 
        WHERE name = ?
        """, (name,)
        )
        
        return cursor.fetchone()
    
    
    @staticmethod
    def delete(name):
        
        cursor.execute(
        """
        DELETE FROM products
        WHERE name = ?
        """, (name,)
        )
        
        connection.commit()