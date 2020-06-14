import sqlite3

import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar

import openfoodfacts

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

def decode_image(file):
    image = cv2.imread(file)
    decode_obj = pyzbar.decode(image)

    if not decode_obj:
        return None

    return str(decode_obj[0].data)

def get_stock():
    select_query = ''' SELECT stock.barcode, name, unit, quantity
                       FROM stock
                       LEFT JOIN products
                       ON stock.barcode = products.barcode
                   '''

    data = connection.execute(select_query)
    return data

# def get_product_info(barcode):
#     product = openfoodfacts.products.get_product(barcode)
#     product = product.get('product')
#     # print((product.get('product')).keys())
#     print(product)
