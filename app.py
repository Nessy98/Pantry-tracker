import tkinter as tk
from frames import get_top_frame, get_bottom_frame

from connection import connection, setup_database, decode_image, get_stock, get_product, update_stock

from time import sleep
from connection import setup_database


def AddToPantry():
    #product_stock = c.execute('SELECT * FROM stock WHERE barcode = "101010"').fetchall()[0]
    # print(row)
    print(quantity.get())

def TakeFromPantry():
    pass
#

# setup_database()

root = tk.Tk()
root.resizable(width=True, height=True)
root.geometry("800x600+89+50")
root.title("Pantry Tracker")


get_top_frame(root)
get_bottom_frame(root)


root.mainloop()
