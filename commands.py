from connection import connection
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
    # camera.capture('capture.jpg')

    # process image and extract barcode
    barcode = '101010'

    return connection.execute('SELECT p.*, s.quantity FROM products AS p LEFT JOIN stock AS s ON p.barcode=s.barcode WHERE p.barcode = ?', (barcode, )).fetchone()


