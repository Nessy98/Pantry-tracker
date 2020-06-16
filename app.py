import types
import tkinter as tk

from frames import get_window, get_top_frame, get_bottom_frame

root = get_window()
get_top_frame(root)
get_bottom_frame(root)

root.mainloop()
