import sqlite3

connection = sqlite3.connect('pantry.db')

# Create table
#connection.execute('''CREATE TABLE IF NOT EXISTS foods
#             (barcode text, name text )''')

#c.execute('''INSERT INTO foods
#             VALUES(101010, 'coca-cola')''')

#connection.execute('''CREATE TABLE IF NOT EXISTS stock
#             (barcode text, quantity text)''')
