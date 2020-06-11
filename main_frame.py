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




