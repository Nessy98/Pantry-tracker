import picamera
import RPi.GPIO as GPIO

from functions import decode_image, get_product, update_stock

WIDTH = 640
HEIGHT = 480

camera = picamera.PiCamera()

def start_camera():
    # Setup Camera
    camera.preview_fullscreen = False
    camera.preview_window=(0, 0, 320, 240)
    camera.resolution=(WIDTH, HEIGHT)

    # Start preview
    camera.start_preview()

def scan():
    image_file = './image.png'
    
    # Capture image and close the preview window
    camera.capture(image_file)
    camera.stop_preview()
    
    # Get barcode from the image 
    barcode = decode_image(image_file)
    if barcode is None:
        return None

    return get_product(barcode)


def save_product(product, quantity, form, root, update_products):
    update_stock(product, quantity)
    products_list = root.get_child('top_frame').get_child('products_list')
    update_products(products_list)

    form.grid_forget()
    form.destroy()
