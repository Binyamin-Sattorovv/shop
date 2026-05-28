import sqlite3

connection = sqlite3.connect(
    "shop/database/shop.db" 
)

cursor = connection.cursor()


cursor.execute("""               
CREATE TABLE IF NOT EXISTS products(
    
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    
    name TEXT,
    price INTEGER,
    dona INTEGER,
    product_type TEXT
)
""")

connection.commit()

