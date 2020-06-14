import tkinter as tk
from frames import get_top_frame, get_bottom_frame
from connection import connection, setup_database, decode_image, get_stock
#import RPi.GPIO as GPIO
#import picamera
from time import sleep

# camera = picamera.PiCamera()

def Capture():
    # camera.capture('capture.jpg')
    # process image and extract barcode
    product = connection.execute('SELECT * FROM foods WHERE barcode = "101010"').fetchall()[0]
    tk.Label(root.frame, text="Add %s to pantry:" % "cola").grid(row=3, column=1)
    tk.Label(root.frame, text="Quantity:").grid(row=4, column=1)
    quantity = tk.Entry(root.frame).grid(row=4, column=2)
    tk.Button(root.frame, text='Add', command=AddToPantry).grid(row=4,column=3)

def AddToPantry():
    #product_stock = c.execute('SELECT * FROM stock WHERE barcode = "101010"').fetchall()[0]
    # print(row)
    print(quantity.get())

def TakeFromPantry():
    pass
#

setup_database()
# barcode = decode_image('test.png')
# connection.execute('''INSERT INTO products
#                       VALUES ('23dg556gh44224', 'coca-cola', 'L');
#                    ''')

# connection.execute('''INSERT INTO stock
#                       VALUES ('23dg556gh44224', 2);
#                    ''')
# get_stock()
root = tk.Tk()
root.resizable(width=True, height=True)
root.geometry("800x600+89+50")
root.title("Pantry Tracker")


get_top_frame(root)
get_bottom_frame(root)


root.mainloop()
