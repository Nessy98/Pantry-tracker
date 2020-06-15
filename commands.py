from connection import connection, decode_image, get_product, update_stock
#import RPi.GPIO as GPIO
#import picamera

# camera = picamera.PiCamera()

def start_camera():
    pass
#    camera.preview_fullscreen=False
#    camera.preview_window=(90,100, 320, 240)
#    camera.resolution=(640,480)
#    camera.start_preview()

def scan():
    image_file = './image.png'
    # camera.capture(image_file)
    barcode = decode_image(image_file)
    return get_product(barcode)


def save_product(product, quantity, form, root, update_products):
    update_stock(product, quantity)
    products_list = root.get_child('top_frame').get_child('products_list')
    update_products(products_list)
    form.grid_forget()
    form.destroy()

