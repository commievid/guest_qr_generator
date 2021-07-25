import epd4in2
from PIL import Image, ImageDraw, ImageFont
import logging
import time

logging.basicConfig(level = logging.INFO)

def draw_qr(ssid, ssid_key):
    logging.info("Starting drawing to e-Paper")

    epd = epd4in2.EPD()
    logging.info("Initialising and clearing display")
    epd.init()
    epd.Clear()

    logging.info("Reading in the PNG file and saving to BMP")
    Image.open("qr.png").resize((300, 300)).save("qr.bmp")
    qrImage = Image.open("qr.bmp")

    logging.info("Begin drawing")
    resultingImage = Image.new("1", (epd.height, epd.width), 255)
    resultingImage.paste(qrImage, (0, 100))

    font18 = ImageFont.truetype("Font.ttc", 18)
    draw = ImageDraw.Draw(resultingImage)
    draw.text((100,0), "Guest Wifi", font = font18, fill = 0)
    draw.text((5,20), "SSID: " + ssid, font = font18, fill = 0)
    draw.text((5,40), "Password: " + ssid_key, font = font18, fill = 0)

    logging.info("Display to e-Paper")
    epd.display(epd.getbuffer(resultingImage))

    time.sleep(2)
    logging.info("Send sleep to e-Paper")
    epd.sleep()

