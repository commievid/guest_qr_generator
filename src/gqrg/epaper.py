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

    title = "Guest Wifi"
    ssid_text = "SSID: " + ssid
    ssid_key_text = "Password: " + ssid_key

    font20 = ImageFont.truetype("forgotten futurist bd.ttf", 20)
    draw = ImageDraw.Draw(resultingImage)

    textSize = draw.textsize(title, font = font20)
    draw.text(((epd.width - textSize[0])/ 2, 0), title, font = font20)
    textSize = draw.textsize(ssid_text, font = font20)
    draw.text(((epd.width - textSize[0])/ 2, 30), ssid_text, font = font20)
    textSize = draw.textsize(ssid_key_text, font = font20)
    draw.text(((epd.width - textSize[0])/ 2, 60), ssid_key_text, font = font20)

    logging.info("Display to e-Paper")
    epd.display(epd.getbuffer(resultingImage))

    time.sleep(2)
    logging.info("Send sleep to e-Paper")
    epd.sleep()

