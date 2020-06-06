import tkinter as tk

def CameraOFF():
    pass
#   camera.stop_preview()

def CameraON():
#    camera.preview_fullscreen=False
#    camera.preview_window=(90,100, 320, 240)
#    camera.resolution=(640,480)
#    camera.start_preview()
    tk.Button(root.frame, text='Capture', command=Capture).grid(row=2,column=1)

def get_main_frame(root):
    frame = tk.Frame(root)
    frame.grid(row=5, column=2)
    tk.Button(frame, text='Add to pantry', command=CameraON).grid(row=1, column = 1)
    tk.Button(frame, text='Take from pantry', command=CameraOFF).grid(row=1, column = 2)
    return frame

