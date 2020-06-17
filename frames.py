import types

import tkinter as tk
from tkinter import ttk

from functions import get_stock
from commands import start_camera, scan, save_product

def patch_frame(target):
    def get_child(self, name):
        return [child for child in self.winfo_children() if child.name == name][0]

    target.get_child = types.MethodType(get_child, target)

def get_window():
    root = tk.Tk()
    
    # Setup root
    root.resizable(width=True, height=True)
    root.geometry("800x350+89+50")
    root.title("Pantry Tracker")

    patch_frame(root)

    return root

def get_top_frame(root):
    frame = tk.Frame(root)
    frame.name = 'top_frame'

    patch_frame(frame)

    frame.root = root
    frame.config(background='#3E4eee')
    frame.pack(side = tk.TOP, expand = False, fill = tk.X)

    cols = ('Name', 'Quantity', 'Unit')
    products_list = ttk.Treeview(frame, columns=cols, show='headings')
    products_list.name = 'products_list'

    products_list.heading("Name", text="Name")
    products_list.column("Name", minwidth=0, width=400, stretch=tk.NO)

    products_list.heading("Quantity", text="Quantity")
    products_list.column("Quantity", minwidth=0, width=200, stretch=tk.NO)

    products_list.heading("Unit", text="Unit")
    products_list.column("Unit", minwidth=0, width=200, stretch=tk.NO)

    update_products_list(products_list)

def update_products_list(products_list):
    products_list.delete(*products_list.get_children())
    stock = get_stock()
    for i, (barcode, name, unit, quantity) in enumerate(stock, start=1):
        products_list.insert("", "end", values=(name, quantity, unit))

    products_list.pack(expand = True, fill = tk.X)

def get_bottom_frame(root):
    frame = tk.Frame(root, highlightbackground='#3E4149', highlightthickness=1, borderwidth=2)
    frame.name = 'bottom_frame'
    frame.root = root

    patch_frame(frame)

    frame.pack(side = tk.BOTTOM, expand = True, fill = tk.BOTH)
    frame.config(background='#3E4149')

    start_scanner_btn = tk.Button(frame, highlightbackground='#3E4149', text="Start Scanner", command=start_camera, fg="black")
    start_scanner_btn.grid(row = 0,column = 0, sticky='w')
    
    scan_btn = tk.Button(frame, highlightbackground='#3E4149', text="Scan",
                         command=lambda: get_product_form(frame, scan()), fg="black"
                        )
    scan_btn.grid(row = 0, column = 1, sticky='w', columnspan=4)

def get_product_form(parent, product):
    frame = tk.Frame(parent, highlightbackground='#3E4149', highlightthickness=1, borderwidth=2)
    frame.grid(row=1, column=0)
    frame.config(background='#3E4149')

    barcode_label = tk.Label(frame ,text = "Barcode: %s " % product['barcode'], justify=tk.LEFT)
    barcode_label.grid(row = 0,column = 0, sticky='w')
    barcode_label.config(background='#3E4149')

    name_label = tk.Label(frame ,text = "Product name:", justify=tk.LEFT)
    name_label.grid(row = 1,column = 0, sticky='w')
    name_label.config(background='#3E4149')

    unit_label = tk.Label(frame ,text = "Unit:", justify=tk.LEFT)
    unit_label.grid(row = 2,column = 0, sticky='w')
    unit_label.config(background='#3E4149')

    qty_label = tk.Label(frame ,text = "Quantity:", justify=tk.LEFT)
    qty_label.grid(row = 3,column = 0, sticky='w')
    qty_label.config(background='#3E4149')

    name_entry = tk.Entry(frame, highlightthickness=1, borderwidth=0)
    name_entry.grid(row = 1, column = 1, columnspan=3, sticky='we')
    name_entry.config(background='#3E4149', highlightbackground="black", highlightcolor="black")
    name_entry.insert(0, product['name'])

    unit_var = tk.StringVar(None, product['unit'])
    unit_var.set(product['unit'])

    liter_btn = tk.Radiobutton(frame,
        indicatoron=0,
        text="Liter",
        padx =20,
        variable=unit_var,
        value="L"
    )

    liter_btn.grid(row=2, column=1)
    liter_btn.config(background='#3E4149', highlightbackground="black", highlightcolor="black")

    kg_btn = tk.Radiobutton(frame,
        indicatoron=0,
        text="Kilogram",
        padx = 20,
        variable=unit_var,
        value="KG"
    )

    kg_btn.grid(row=2, column=3)
    kg_btn.config(background='#3E4149', highlightbackground="black", highlightcolor="black")

    qty_entry = tk.Entry(frame, highlightthickness=1, borderwidth=0)
    qty_entry.grid(row = 3,column = 1, columnspan=3, sticky='we')
    qty_entry.config(background='#3E4149', highlightbackground="black", highlightcolor="black")
    qty_entry.insert(0, product['quantity'])

    save_btn = tk.Button(frame, highlightbackground='#3E4149', 
                         command=lambda: save_product(product, qty_entry.get(), frame, parent.root, update_products_list),
                         text="Save", fg="black"
                        )
    save_btn.grid(row=0, column=4, columnspan=4, sticky='we')
