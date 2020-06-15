import types
import tkinter as tk
from frames import get_window, get_top_frame, get_bottom_frame
from connection import connection, setup_database, decode_image, get_stock, get_product, update_stock

root = get_window()
get_top_frame(root)
get_bottom_frame(root)

root.mainloop()
