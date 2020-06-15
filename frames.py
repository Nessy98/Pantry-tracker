import tkinter as tk
from tkinter import ttk
from commands import start_camera, scan



def get_top_frame(root):
    frame = tk.Frame(root)
    frame.config(background='#3E4eee')
    frame.pack(side = tk.TOP, expand = True, fill = tk.BOTH)

    cols = ('Name', 'Quantity', 'Unit')
    products_list = ttk.Treeview(frame, columns=cols, show='headings')

    products_list.heading("Name", text="Name")
    products_list.column("Name", minwidth=0, width=400, stretch=tk.NO)

    products_list.heading("Quantity", text="Quantity")
    products_list.column("Quantity", minwidth=0, width=200, stretch=tk.NO)

    products_list.heading("Unit", text="Unit")
    products_list.column("Unit", minwidth=0, width=200, stretch=tk.NO)

    tempList = [['Coca-Cola', '10', 'Liter'], ['Cheese', '0.500', 'Kg'],
            ['Pork shoulder', '1.4', 'Kg']]
    for i, (name, quantity, unit) in enumerate(tempList, start=1):
        products_list.insert("", "end", values=(name, quantity, unit))

    products_list.pack(expand = True, fill = tk.BOTH)


def get_bottom_frame(root):
    frame = tk.Frame(root, highlightbackground='#3E4149', highlightthickness=1, borderwidth=2)
    frame.pack(side = tk.BOTTOM, expand = True, fill = "x")
    frame.config(background='#3E4149')

    start_scanner_btn = tk.Button(frame, highlightbackground='#3E4149', text="Start Scanner", command=start_camera, fg="black")
    start_scanner_btn.pack( side = tk.TOP)

    scan_btn = tk.Button(frame, highlightbackground='#3E4149', text="Scan", command=lambda: get_product_form(frame, scan()), fg="black")
    scan_btn.pack( side = tk.TOP)

def get_product_form(root, product):
    print(product)
    (barcode, name, unit, quantity) = product

    frame = tk.Frame(root, highlightbackground='#3E4149', highlightthickness=1,  borderwidth=2)
    frame.pack(side = tk.BOTTOM, expand = True, fill = "x")
    frame.config(background='#3E4149')

    name_label = tk.Label(frame ,text = "Product name:", justify=tk.LEFT)
    name_label.grid(row = 0,column = 0, sticky='w')
    name_label.config(background='#3E4149')

    unit_label = tk.Label(frame ,text = "Unit:", justify=tk.LEFT)
    unit_label.grid(row = 1,column = 0, sticky='w')
    unit_label.config(background='#3E4149')

    qty_label = tk.Label(frame ,text = "Quantity:", justify=tk.LEFT)
    qty_label.grid(row = 2,column = 0, sticky='w')
    qty_label.config(background='#3E4149')

    name_entry = tk.Entry(frame, highlightthickness=1, borderwidth=0)
    name_entry.grid(row = 0, column = 1, columnspan=3, sticky='we')
    name_entry.config(background='#3E4149', highlightbackground = "black", highlightcolor= "black")#, state="readonly")
    name_entry.insert(0, name)


    unit_var = tk.StringVar()
    unit_var.set(unit)

    liter_btn = tk.Radiobutton(frame,
        indicatoron=0,
        text="Liter",
        padx = 20,
        variable=unit_var,
        value=unit
    )
    liter_btn.grid(row=1, column=1)
    liter_btn.config(background='#3E4149', highlightbackground = "black", highlightcolor= "black")

    kg_btn = tk.Radiobutton(frame,
        indicatoron=0,
        text="Kilogram",
        padx = 20,
        variable=unit_var,
        value="KILOGRAM"
    )
    kg_btn.grid(row=1, column=3)
    kg_btn.config(background='#3E4149', highlightbackground = "black", highlightcolor= "black")

    qty_entry = tk.Entry(frame, highlightthickness=1, borderwidth=0)
    qty_entry.grid(row = 2,column = 1, columnspan=3, sticky='we')
    qty_entry.config(background='#3E4149', highlightbackground = "black", highlightcolor= "black")
    qty_entry.insert(0, quantity)

    save_btn = tk.Button(frame, highlightbackground='#3E4149', text="Save", fg="black")
    save_btn.grid(row=3, column=0, columnspan=4, sticky='we')
