import tkinter as tk
from main_frame import get_main_frame
from connection import connection
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

root = tk.Tk()
root.resizable(width=False, height=False)
root.geometry("320x300+89+50")
root.title("Pantry Tracker")

root.frame = get_main_frame(root)
root.mainloop()
