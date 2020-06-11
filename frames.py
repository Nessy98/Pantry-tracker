import tkinter as tk
from tkinter import ttk



def get_top_frame(root):
    frame = tk.Frame(root)
    frame.config(background='#3E4eee')
    frame.pack(side = tk.TOP, expand = True, fill = tk.BOTH)

    cols = ('Name', 'Quantity', 'Unit')
    listBox = ttk.Treeview(frame, columns=cols, show='headings')

    listBox.heading("Name", text="Name")
    listBox.column("Name", minwidth=0, width=400, stretch=tk.NO)

    listBox.heading("Quantity", text="Quantity")
    listBox.column("Quantity", minwidth=0, width=200, stretch=tk.NO)

    listBox.heading("Unit", text="Unit")
    listBox.column("Unit", minwidth=0, width=200, stretch=tk.NO)

    tempList = [['Coca-Cola', '10', 'Liter'], ['Cheese', '0.500', 'Kg'],
            ['Pork shoulder', '1.4', 'Kg']]
    for i, (name, quantity, unit) in enumerate(tempList, start=1):
        listBox.insert("", "end", values=(name, quantity, unit))

    listBox.pack(expand = True, fill = tk.BOTH)




def get_bottom_frame(root):
    bottomframe = tk.Frame(root, highlightbackground='#3E4149', highlightcolor="green", highlightthickness=1, width=100, height=100, bd= 0)
    bottomframe.pack(side = tk.BOTTOM, expand = True, fill = tk.BOTH)
    bottomframe.config(background='#3E4149')
    blackbutton = tk.Button(bottomframe, highlightbackground='#3E4149', text="Scan", fg="black")
    blackbutton.pack( side = tk.TOP)


