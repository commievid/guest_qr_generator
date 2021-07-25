import epd4in2
from PIL import Image
import logging
import time

logging.basicConfig(level = logging.INFO)

def draw_qr():
    logging.info("Starting drawing to e-Paper")

    epd = epd4in2.EPD()
    logging.info("Initialising and clearing display")
    epd.init()
    epd.Clear()

    logging.info("Reading in the PNG file")
    qrImage = Image.open("qr.png")
    epd.display(epd.getbuffer(qrImage))

    time.sleep(2)
    logging.info("Send sleep to e-Paper")
    epd.sleep()

