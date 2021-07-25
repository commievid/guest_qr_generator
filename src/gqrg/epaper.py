import epd4in2
from PIL import Image, ImageDraw, ImageFont
import logging
import time

logging.basicConfig(level = logging.INFO)

def draw_qr():
    logging.info("Starting drawing to e-Paper")

    epd = epd4in2.EPD()
    logging.info("Initialising and clearing display")
    epd.init()
    epd.Clear()

    logging.info("Reading in the PNG file and saving to BMP")
    Image.open("qr.png").save("qr.bmp")
    qrImage = Image.open("qr.bmp")
    qrImage.resize((300, 300))

    resultingImage = Image.new("1", (epd.height, epd.width), 255)
    resultingImage.paste(qrImage, (50, 0))

    font18 = ImageFont.truetype("Font.ttc", 18)
    draw = ImageDraw.Draw(resultingImage)
    draw.text((0,0), "Test!", font = font18, fill = 0)

    epd.display(epd.getbuffer(resultingImage))

    time.sleep(2)
    logging.info("Send sleep to e-Paper")
    epd.sleep()

