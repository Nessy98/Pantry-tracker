import sqlite3

connection = sqlite3.connect('pantry.db')

def setup_database():
    # Product table create statement
    product_query = '''CREATE TABLE IF NOT EXISTS products (
                        barcode TEXT PRIMARY KEY,
                        name TEXT NOT NULL,
                        unit TEXT NOT NULL
                    );'''
    # Stock table create statement
    stock_query = '''CREATE TABLE IF NOT EXISTS stock (
                        barcode TEXT PRIMARY KEY,
                        quantity REAL,
                        FOREIGN  KEY (barcode)
                            REFERENCES products (barcode)
                    );'''

    # Create tables products and stock
    connection.execute(product_query)
    connection.execute(stock_query)

#c.execute('''INSERT INTO foods
#             VALUES(101010, 'coca-cola')''')
